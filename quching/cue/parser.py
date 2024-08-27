import taglib
import re
import os
from difflib import SequenceMatcher
from .cuesheet import CueSheet

COMMANDS = {}

def command(com):
    def __decorator(f):
        COMMANDS[com] = f
        return f
    return __decorator

IGNORED_COMMANDS = [
    "REM",
    "CATALOG",
    "CDTEXTFILE",
    "FLAGS",
    "ISRC",
    "POSTGAP",
    "PREGAP",
    "SONGWRITER"
] # these commands aren't useful in our case so we can safely ignore them

EXTENSIONS = [".flac", ".mp3", ".wav", ".ogg", ".m4a", ".aac", ".alac"]

def parse(file):
    cue_sheet = CueSheet(file)
    with open(file, errors="ignore") as sheet:
        for line in sheet.readlines():
            try:
                comm, params = parse_command(line.strip())
                if comm in IGNORED_COMMANDS:
                    continue
                COMMANDS[comm](params, cue_sheet)
            except Exception:
                return None
        cue_sheet = check_files(cue_sheet)
        return cue_sheet if check_cue(cue_sheet) else None

def parse_url(url):
    return re.findall(r"cue://(.*.cue)/([0-9]*)", url)[0]

def check_cue(cue):
    sheet_ok =  all(cue.__dict__) # check for null values in the CueSheet fields
    tracks_ok = all(all(v is not None for v in t.__dict__.values()) for t in cue.tracks) # checks all the fields of the tracks for null values
    compliant = all(not any(t1.file == t2.file and t1.timestamp == 0 and t2.timestamp == 0 and t1.title != t2.title for t2 in cue.tracks) for t1 in cue.tracks) # some sheets (mostly those produced by EAC) may be non-compliant because of gaps appended to the previous file
    files_ok = all(os.path.splitext(f)[1].lower() in EXTENSIONS for f in cue.files)
    return sheet_ok and tracks_ok and compliant and files_ok

def check_files(cue): # it seems that files in a cue sheet can have the wrong extension and it should still work, wtf?
    directory = os.path.dirname(cue.cue_file)
    files_in_dir = os.listdir(directory)
    files_in_dir.remove(os.path.basename(cue.cue_file))
    new_files = []
    for f in cue.files:
        if f not in files_in_dir:
            closest_file = sorted(files_in_dir, key=lambda x: SequenceMatcher(None, f, x).ratio(), reverse=True)[0]
            new_files.append(closest_file)
            for t in cue.tracks:
                if t.file == f:
                    t.file = closest_file
        else:
            new_files.append(f)
    cue.files = new_files
    return cue

def parse_command(line):
    regex = r"^([A-Z]+)\s+(.*)$"
    res = re.findall(regex, line)
    command = res[0][0]
    params = parse_params(res[0][1])
    return command, params

def parse_params(string):
    params = []

    if string[0] == '"':
        end_quote = string.index('"', 1)
        params.append(string[1:end_quote])
        string = string[end_quote+1:]
    
    if string != '':
        params += string.split(" ")

    return params

def index_to_sec(index):
    mins, secs, frames = index.split(":")
    return int(mins) * 60 + int(secs) + round(int(frames) / 75)

@command("FILE")
def parse_file(params, cue):
    cue.add_file(params[0])

@command("INDEX")
def parse_index(params, cue):
    if params[0] != "01": # other indexes indicate pre/post gap, real beginning is at index 01
        return
    cue.set_track_timestamp(index_to_sec(params[1]))

@command("PERFORMER")
def parse_performer(params, cue):
    if cue.artist is None:
        cue.set_artist(params[0])
    else:
        cue.set_track_artist(params[0])

@command("TITLE")
def parse_title(params, cue):
    if cue.title is None:
        cue.set_title(params[0])
    else:
        cue.set_track_title(params[0])

@command("TRACK")
def parse_track(params, cue):
    cue.add_track(int(params[0]))