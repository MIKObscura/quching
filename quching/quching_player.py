from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PySide6.QtCore import QObject, QUrl


class QuchingPlayer(QObject):
    
    def __init__(self, path, volume=1):
        self.queue = [path]
        self.current_track = 0
        self.player = QMediaPlayer()
        self.output = QAudioOutput()
        self.output.setVolume(volume)
        self.player.setAudioOutput(self.output)
        self.player.setSource(QUrl.fromLocalFile(path))
    
    def get_metadata(self):
        return self.player.metaData()
    
    def play_next(self):
        if self.current_track + 1 >= len(self.queue):
            self.current_track = 0
        else:
            self.current_track += 1
        self.player.stop()
        self.player.setSource(QUrl.fromLocalFile(self.queue[self.current_track]))
    
    def play_previous(self):
        if self.current_track - 1 < 0:
            self.current_track = len(self.queue) - 1
        else: 
            self.current_track -= 1
        self.player.stop()
        self.player.setSource(QUrl.fromLocalFile(self.queue[self.current_track]))
    
    def toggle_play(self):
        if self.player.isPlaying():
            self.player.pause()
        else:
            self.player.play()