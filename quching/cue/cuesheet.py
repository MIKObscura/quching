from dataclasses import dataclass, field

@dataclass
class Track:
    tracknumber: int
    file: str
    title: str = None
    timestamp: int = None
    duration: int = None
    artist: str = None


class CueSheet:
    
    def __init__(self, filename):
        self.cue_file = filename
        self.files = []
        self.tracks = []
        self.title = None
        self.artist = None
    
    def add_file(self, file):
        self.files.append(file)
    
    def add_track(self, tracknumber):
        self.tracks.append(Track(file=self.files[-1], tracknumber=tracknumber))
    
    def set_track_title(self, title):
        self.tracks[-1].title = title
    
    def set_track_timestamp(self, timestamp):
        self.tracks[-1].timestamp = timestamp
        if len(self.tracks) == 1:
            self.tracks[-1].duration = timestamp
        else:
            self.tracks[-1].duration = timestamp - self.tracks[-2].timestamp
    
    def set_track_artist(self, artist):
        self.tracks[-1].artist = artist
    
    def set_artist(self, artist):
        self.artist = artist
    
    def set_title(self, title):
        self.title = title