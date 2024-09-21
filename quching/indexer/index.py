import glob
from pathlib import Path
import sqlite3
import os
import taglib
from itertools import chain
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
    blacklist = open(os.path.join(str(Path("~").expanduser()), ".config/quching/blacklist.txt"), "a+")
    blacklisted_files = open(os.path.join(str(Path("~").expanduser()), ".config/quching/blacklist.txt"), "r").readlines()
    parsed_cues = []
    for c in cues:
        if c + "\n" in blacklisted_files:
            continue
        res = parser.parse(c)
        if res is not None:
            parsed_cues.append(res)
        else:
            blacklist.write(c + "\n")
    blacklist.close()
    return parsed_cues


def get_tracknumber(string):
    try:
        return int(string)
    except ValueError:
        return int(string.split("/")[0])

def get_all_files_in_cues(cues):
    return list(chain.from_iterable(map(lambda x: x.files, cues)))

def make_index():
    if "index.db" not in os.listdir("."):
        db.create_db()
    files = find_files()
    cues = find_cues()
    cues = parse_cues(cues)
    cue_files = get_all_files_in_cues(cues)
    files = [file for file in files if os.path.basename(file) not in cue_files]
    index_cues(cues)
    index_files(files)

def index_files(files):
    blacklist = open(os.path.join(str(Path("~").expanduser()), ".config/quching/blacklist.txt"), "a+")
    blacklisted_files = open(os.path.join(str(Path("~").expanduser()), ".config/quching/blacklist.txt"), "r").readlines()
    for f in files:
        if f + "\n" in blacklisted_files:
            continue
        fileTags = taglib.File(f)
        meta = fileTags.tags
        artist = ""
        album = ""
        title = ""
        year = get_year(meta)
        genre = get_genre(meta)
        duration = fileTags.length
        try:
            artist = " & ".join(meta["ARTIST"])
        except KeyError:
            blacklist.write(f + "\n")
            continue
        try:
            title = meta["TITLE"][0]
        except (KeyError, IndexError):
            blacklist.write(f + "\n")
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
        db.insert_file(f, artist, album, title, duration, tracknumber, year, genre)

def get_year(tags):
    if "DATE" in tags and len(tags["DATE"]) > 0:
        if "-" in tags["DATE"][0]: # so many different formats!
            return int(tags["DATE"][0].split("-")[0])
        if "/" in tags["DATE"][0]:
            return int(tags["DATE"][0].split(" / ")[0])
        return int(tags["DATE"][0])
    if "YEAR" in tags and len(tags["YEAR"]) > 0:
        return int(tags["YEAR"][0])
    return None

def get_genre(tags):
    if "GENRE" in tags and len(tags["GENRE"]) > 0:
        return tags["GENRE"][0]
    return None

def index_cues(cues):
    for c in cues:
        for t in c.tracks:
            db.insert_cue(c.cue_file, t.tracknumber,t.file, t.artist, c.title, t.title, t.duration, t.timestamp, c.year, c.genre)

def refresh_index():
    if "index.db" not in os.listdir("."):
        make_index()
        return
    local_files = find_files()
    local_cues = find_cues()
    local_cues = parse_cues(local_cues)
    local_cue_files = get_all_files_in_cues(local_cues)
    local_files = [file for file in local_files if os.path.basename(file) not in local_cue_files]
    db_files = db.get_all_files()
    db_cues = db.get_all_cues()
    new_files = list(set(local_files).difference(db_files))
    index_files(new_files)
    removed_files = list(set(db_files).difference(local_files))
    for f in removed_files:
        db.delete_file(f)
    new_cues = list(set([c.cue_file for c in local_cues]).difference(db_cues))
    index_cues(parse_cues(new_cues))
    removed_cues = list(set(db_cues).difference([c.cue_file for c in local_cues]))
    for c in removed_cues:
        db.delete_cue(c)