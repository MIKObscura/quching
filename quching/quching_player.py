from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PySide6.QtCore import QObject, QUrl


class QuchingPlayer(QObject):
    
    def __init__(self, paths, volume=1):
        self.queue = paths
        self.current_track = 0
        self.player = QMediaPlayer()
        self.output = QAudioOutput()
        self.output.setVolume(volume)
        self.player.setAudioOutput(self.output)
        self.player.setSource(QUrl.fromLocalFile(self.queue[0]))
    
    def get_metadata(self):
        return self.player.metaData()
    
    def play_next(self):
        was_playing = self.player.isPlaying()
        if self.current_track + 1 >= len(self.queue):
            self.current_track = 0
        else:
            self.current_track += 1
        self.player.setSource(QUrl.fromLocalFile(self.queue[self.current_track]))
        if was_playing:
            self.player.play()
    
    def play_previous(self):
        was_playing = self.player.isPlaying()
        if (self.player.position() / self.player.duration()) < 0.5:
            if self.current_track - 1 < 0:
                self.current_track = len(self.queue) - 1
            else: 
                self.current_track -= 1
            self.player.setSource(QUrl.fromLocalFile(self.queue[self.current_track]))
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