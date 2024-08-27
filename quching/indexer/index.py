import glob
from pathlib import Path
import sqlite3
import os
import taglib
import quching.indexer.database as db
from quching.cue import parser

EXTENSIONS = ["flac", "mp3", "wav", "ogg", "m4a", "aac", "alac"]

def find_files():
    files = []
    for e in EXTENSIONS:
        files += glob.glob(str(Path("~").expanduser()) + F"/Music/**/*.{e}", recursive=True)
    return files

def find_cues():
    return glob.glob(str(Path("~").expanduser()) + F"/Music/**/*.cue", recursive=True)

def parse_cues(cues):
    parsed_cues = []
    for c in cues:
        res = parser.parse(c)
        if res is not None:
            parsed_cues.append(res)
    return parsed_cues


def get_tracknumber(string):
    try:
        return int(string)
    except ValueError:
        return int(string.split("/")[0])

def get_all_files_in_cues(cues):
    files = []
    for c in cues:
        files += c.files
    return files

def make_index():
    if "index.db" not in os.listdir("."):
        db.create_db()
    files = find_files()
    cues = find_cues()
    cues = parse_cues(cues)
    cue_files = get_all_files_in_cues(cues)
    files = [file for file in files if file not in cue_files]
    index_cues(cues)
    #index_files(files)

def index_files(files):
    for f in files:
        fileTags = taglib.File(f)
        meta = fileTags.tags
        artist = ""
        album = ""
        title = ""
        duration = fileTags.length
        try:
            artist = " & ".join(meta["ARTIST"])
        except KeyError:
            continue
        try:
            title = meta["TITLE"][0]
        except (KeyError, IndexError):
            continue
        try:
            album = meta["ALBUM"][0]
        except (KeyError, IndexError):
            album = meta["TITLE"][0]
        tracknumber = 1
        try:
            tracknumber = get_tracknumber(meta["TRACKNUMBER"][0])
        except (KeyError, IndexError):
            tracknumber = 1
        db.insert_file(f, artist, album, title, duration, tracknumber)
    
def index_cues(cues):
    for c in cues:
        for t in c.tracks:
            db.insert_cue(c.cue_file, t.file, t.artist, c.title, t.title, t.duration, t.timestamp)