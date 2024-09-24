from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PySide6.QtCore import QObject, QUrl
from quching.cue import parser
from random import sample
import os


class QuchingPlayer(QObject):
    
    def __init__(self, paths, volume=1):
        self.queue = paths
        self.unshuffled_queue = paths
        self.current_track = 0
        self.player = QMediaPlayer()
        self.output = QAudioOutput()
        self.shuffle = False
        self.repeat = False
        self.output.setVolume(volume)
        self.player.setAudioOutput(self.output)
        if self.queue:
            self.player.setSource(QUrl.fromLocalFile(self.queue[0]))
    
    def get_metadata(self):
        return self.player.metaData()
    
    def play_next(self):
        was_playing = self.player.isPlaying()
        if len(self.queue) == 0:
            self.player.stop()
            return
        if self.repeat:
            self.player.setPosition(0)
            if was_playing:
                self.player.play()
            return
        if self.current_track + 1 >= len(self.queue):
            self.current_track = 0
        else:
            self.current_track += 1
        if self.get_current_track().startswith("cue://"):
            cue_file, tracknumber = parser.parse_url(self.get_current_track())
            cue_sheet = parser.parse(cue_file)
            track = cue_sheet.tracks[int(tracknumber) - 1]
            self.player.setSource(QUrl.fromLocalFile(os.path.join(os.path.dirname(cue_file), track.file)))
        else:
            self.player.setSource(QUrl.fromLocalFile(self.get_current_track()))
        if was_playing:
            self.player.play()
    
    def play_previous(self):
        was_playing = self.player.isPlaying()
        if len(self.queue) == 0:
            self.player.stop()
            return
        if self.repeat:
            self.player.setPosition(0)
            if was_playing:
                self.player.play()
            return
        if (self.player.position() / self.player.duration()) < 0.5:
            if self.current_track - 1 < 0:
                self.current_track = len(self.queue) - 1
            else: 
                self.current_track -= 1
            if self.get_current_track().startswith("cue://"):
                cue_file, tracknumber = parser.parse_url(self.get_current_track())
                cue_sheet = parser.parse(cue_file)
                track = cue_sheet.tracks[int(tracknumber) - 1]
                self.player.setSource(QUrl.fromLocalFile(os.path.join(os.path.dirname(cue_file), track.file)))
            else:
                self.player.setSource(QUrl.fromLocalFile(self.get_current_track()))
            if was_playing:
                self.player.play()
        else:
            self.player.setPosition(0)
            if was_playing:
                self.player.play()
    
    def toggle_play(self):
        if self.player.isPlaying():
            self.player.pause()
        else:
            self.player.play()
    
    def get_current_track(self):
        return self.queue[self.current_track]
    
    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        if self.shuffle:
            shuffled_queue = sample(self.queue, len(self.queue))
            current_track = shuffled_queue.index(self.get_current_track())
            shuffled_queue.insert(0, shuffled_queue.pop(current_track))
            self.unshuffled_queue = self.queue.copy()
            self.queue = shuffled_queue.copy()
            self.current_track = 0
        else:
            current_track = self.unshuffled_queue.index(self.get_current_track())
            self.queue = self.unshuffled_queue.copy()
            self.current_track = current_track

    def toggle_repeat(self):
        self.repeat = not self.repeat