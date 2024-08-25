from dataclasses import dataclass, field

@dataclass
class Track:
    tracknumber: int
    file: str
    title: str = ""
    timestamp: int = 0
    artist: str = ""


class CueSheet:
    
    def __init__(self, filename):
        self.cue_file = filename
        self.files = []
        self.tracks = []
    
    def add_file(self, file):
        self.files.append(file)
    
    def add_track(self, tracknumber):
        self.tracks.append(Track(file=self.files[-1], tracknumber=tracknumber))
    
    def set_track_title(self, title):
        self.tracks[-1].title = title
    
    def set_track_timestamp(self, timestamp):
        self.tracks[-1].timestamp = timestamp
    
    def set_track_artist(self, artist):
        self.tracks[-1].artist = artist
    
    def set_artist(self, artist):
        self.artist = artist
    
    def set_title(self, title):
        self.title = title