import glob
from pathlib import Path
import sqlite3
import os
import taglib
import quching.indexer.database as db

EXTENSIONS = ["flac", "mp3", "wav", "ogg", "m4a", "aac", "alac"]

def find_files():
    files = []
    for e in EXTENSIONS:
        files += glob.glob(str(Path("~").expanduser()) + F"/Music/**/*.{e}", recursive=True)
    return files

def get_tracknumber(string):
    try:
        return int(string)
    except ValueError:
        return int(string.split("/")[0])

def make_index():
    if "index.db" not in os.listdir("."):
        db.create_db()
    files = find_files()
    index_files(files)

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