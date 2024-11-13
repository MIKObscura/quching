import sqlite3
import os

def insert_file(filename, artist, album, title, duration, tracknumber, year, genre):
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.execute("insert into audio_files (filename, artist, album, title, duration, tracknumber, year, genre) values (?, ?, ?, ?, ?, ?, ?, ?)",
        (filename, artist, album, title, duration, tracknumber, year, genre))
    index.commit()
    index.close()

def insert_cue(cue, tracknumber, file, artist, album, title, duration, timestamp, year, genre):
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.execute("insert into cue_sheets (cue, tracknumber, filename, artist, album, title, duration, timestamp, year, genre) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (cue, tracknumber, file, artist, album, title, duration, timestamp, year, genre))
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

def get_all_tracks():
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    tracks = index_cur.execute("select * from audio_files").fetchall()
    index.close()
    return tracks

def get_all_cue_tracks():
    if not os.path.exists("index.db"):
        return []
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    tracks = index_cur.execute("select * from cue_sheets").fetchall()
    index.close()
    return tracks

def create_db():
    index = sqlite3.connect("index.db")
    index_cur = index.cursor()
    index_cur.executescript(open("createdb.sql").read())
    index.commit()
    index.close()

def search_db(selectors, limit=None):
    search_string = ""
    placeholders = []
    for s in selectors:
        if type(s) in (list, tuple):
            if s[1] == "=":
                search_string += F"{s[0]} LIKE ?"
            else:
                search_string += F"{s[0]} NOT LIKE ?"
            placeholders.append(s[2])
        else:
            search_string += F" {s} "
    index = sqlite3.connect("index.db")
    index.row_factory = sqlite3.Row
    index_cur = index.cursor()
    query = index_cur.execute(F"select * from audio_files where {search_string} collate NOCASE", placeholders)
    if limit is not None:
        query = query.fetchmany(limit)
    else:
        query = query.fetchall()
    query_cue = index_cur.execute(F"select * from cue_sheets where {search_string} collate NOCASE", placeholders)
    if limit is not None:
        res = (query + query_cue.fetchmany(limit))[:limit]
        return res
    else:
        return query + query_cue.fetchall()
