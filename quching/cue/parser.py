import taglib
import re
from .cuesheet import CueSheet
from functools import wraps

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
    with open(file) as sheet:
        for line in sheet.readlines():
            comm, params = parse_command(line.strip())

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

@command("FILE")
def parse_file(params):
    return res[0]

@command("INDEX")
def parse_index(params):
    pass

@command("PERFORMER")
def parse_performer(params):
    pass

@command("TITLE")
def parse_title(params):
    pass

@command("TRACK")
def parse_track(params):
    pass