import taglib
import re
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
        return cue_sheet if check_cue(cue_sheet) else None

def check_cue(cue):
    return all(cue.__dict__) and all(all(v is not None for v in t.__dict__.values()) for t in cue.tracks)

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