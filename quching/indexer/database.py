import sqlite3
import os

def insert_file(filename, artist, album, title, duration, tracknumber):
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.execute("insert into audio_files (filename, artist, album, title, duration, tracknumber) values (?, ?, ?, ?, ?, ?)",
        (filename, artist, album, title, duration, tracknumber))
    index.commit()
    index.close()

def insert_cue(cue, file, artist, album, title, duration, timestamp):
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.execute("insert into cue_sheets (cue, filename, artist, album, title, duration, timestamp) values (?, ?, ?, ?, ?, ?, ?)",
    (cue, file, artist, album, title, duration, timestamp))
    index.commit()
    index.close()

def delete_file(file):
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.execute("delete from audio_files where filename = ?", (file,))
    index.commit()
    index.close()

def delete_cue(cue):
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.execute("delete from cue_sheets where cue = ?", (cue,))
    index.commit()
    index.close()

def get_artists():
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    artists = index_cur.execute("select distinct artist \
        from audio_files \
        union select distinct artist from cue_sheets \
        order by artist collate nocase").fetchall()
    index.close()
    return [a["artist"] for a in artists]

def get_albums():
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    albums = index_cur.execute("select artist, album \
        from audio_files \
        group by artist, album \
        order by lower(album)").fetchall()
    albums += index_cur.execute("select artist, album \
        from cue_sheets \
        group by artist, album \
        order by lower(album)").fetchall()
    index.close()
    return sorted(albums, key=lambda a: a[1].lower())

def get_artist_albums(artist):
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    albums = index_cur.execute("select distinct album \
        from audio_files as a \
        where a.artist = ? \
        union select distinct album \
        from cue_sheets as c \
        where c.artist = ?", (artist, artist)).fetchall()
    index.close()
    return albums

def get_album_tracks(artist, album):
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    tracks = index_cur.execute("select filename, title, duration, tracknumber \
        from audio_files \
        where artist=? and album=? \
        order by tracknumber", (artist, album)).fetchall()
    if len(tracks) > 0:
        index.close()
        return tracks
    tracks = index_cur.execute("select cue, filename, title, timestamp, duration \
        from cue_sheets \
        where artist=? and album=? \
        order by timestamp", (artist, album)).fetchall()
    index.close()
    return tracks

def get_track(artist, album):
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    track = index_cur.execute("select filename, title, duration, tracknumber \
        from audio_files \
        where artist=? and album=? \
        order by tracknumber", (artist, album)).fetchone()
    if track is not None:
        index.close()
        return track
    track = index_cur.execute("select cue, filename, title, timestamp, duration \
        from cue_sheets \
        where artist=? and album=? \
        order by timestamp", (artist, album)).fetchone()
    index.close()
    return track

def get_all_files():
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    files = index_cur.execute("select distinct filename from audio_files").fetchall()
    index.close()
    return [f["filename"] for f in files]

def get_all_cues():
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    files = index_cur.execute("select distinct cue from cue_sheets").fetchall()
    index.close()
    return [f["cue"] for f in files]

def create_db():
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.executescript(open("createdb.sql").read())
    index.commit()
    index.close()