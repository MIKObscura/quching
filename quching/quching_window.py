from PySide6.QtCore import (Qt, QSize, QByteArray)
from PySide6.QtGui import (QIcon, QImage, QPixmap, QStandardItemModel, QStandardItem, QShortcut, QKeySequence)
from PySide6.QtWidgets import (QMainWindow, QTreeWidgetItem)
from PySide6.QtMultimedia import QMediaMetaData, QMediaPlayer
from quching.quching_playlist_composer import QuchingPlaylistComposer
from quching.quching_dynamic_playlist_wizard import QuchingDynamicPlaylistWizard
import quching.utils as utils
import taglib
import audio_metadata
import quching.indexer.database as db
import os
import glob
from pathlib import Path
from quching.cue import parser
import json
from quching.gui.quching_ui import Ui_Quching

class QuchingWindow(QMainWindow):
    def __init__(self, player, parent=None):
        super(QuchingWindow, self).__init__(parent)
        self.ui = Ui_Quching()
        self.ui.setupUi(self)
        self.init_ui()
        self.player = player
        self.queue_setup = False
        self.setup_queue()
        self.player.player.mediaStatusChanged.connect(self.load)
        self.ui.play_button.clicked.connect(self.toggle_play)
        self.ui.next_button.clicked.connect(self.player.play_next)
        self.ui.prev_button.clicked.connect(self.player.play_previous)
        self.player.player.sourceChanged.connect(self.change_meta)
        self.player.player.positionChanged.connect(self.update_pos)
        self.ui.seek_slider.sliderMoved.connect(self.seeked)
        self.ui.volume_slider.valueChanged.connect(self.update_vol)
        self.ui.volume_slider.setValue(int(self.player.output.volume() * 100))
        self.ui.volume_percent.setText(F"{self.ui.volume_slider.value()}%")
        self.ui.queue_model.rowsRemoved.connect(self.rearrange_queue)
        self.ui.artists_list.doubleClicked.connect(self.display_artist)
        self.ui.albums_list.doubleClicked.connect(self.display_album)
        self.ui.playlists_list.doubleClicked.connect(self.display_playlist)
        self.ui.dynamic_playlists_list.doubleClicked.connect(self.display_dynamic_playlist)
        self.ui.back_button3.clicked.connect(self.back_to_artists)
        self.ui.back_button2.clicked.connect(self.back_to_albums)
        self.ui.back_button.clicked.connect(self.back_to_playlists)
        self.ui.play_playlist_button.clicked.connect(self.play_playlist)
        self.ui.albums_tree.itemDoubleClicked.connect(self.add_to_queue)
        self.ui.album_tracks.itemDoubleClicked.connect(self.add_to_queue)
        self.ui.playlist_tracks.itemDoubleClicked.connect(self.add_to_queue)
        self.ui.shuffle_button.toggled.connect(self.toggle_shuffle)
        self.ui.repeat_button.toggled.connect(self.player.toggle_repeat)
        self.ui.clear_button.clicked.connect(self.clear_queue)
        self.ui.new_playlist_button.clicked.connect(self.open_playlist_dialog)
        self.ui.edit_playlist_button.clicked.connect(self.edit_playlist)
        self.ui.playlist_page_switcher.activated.connect(self.ui.stacked_playlists_lists.setCurrentIndex)
        self.setup_artists()
        self.setup_albums()
        self.setup_playlists()
        self.setup_dynamic_playlists()
        self.setup_shortcuts()
        self.toggle_play()

    def init_ui(self):
        self.ui.queue_model = QStandardItemModel()
        self.ui.queue_view.setModel(self.ui.queue_model)

        self.ui.artists_model = QStandardItemModel()
        self.ui.artists_list.setModel(self.ui.artists_model)

        self.ui.albums_model = QStandardItemModel()
        self.ui.albums_list.setModel(self.ui.albums_model)

        self.ui.playlists_model = QStandardItemModel()
        self.ui.playlists_list.setModel(self.ui.playlists_model)

        self.ui.dynamic_playlists_model = QStandardItemModel()
        self.ui.dynamic_playlists_list.setModel(self.ui.dynamic_playlists_model)

        self.ui.central_widget.setStyleSheet(
            "#queue_widget { background-image: url(cat.png); background-position: bottom left; background-repeat: no-repeat }")
        self.ui.queue_widget.setStyleSheet(
            "#queue_view { background-color: rgba(0,0,0,0%) } #queue_view::item { padding-top: 5px }")
    
    def load(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.change_meta()
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.play_next()
            self.player.player.play()
    
    def change_meta(self, media=None):
        if self.player.player.mediaStatus() != QMediaPlayer.MediaStatus.LoadedMedia:
            return
        if self.player.get_current_track().startswith("cue://"):
            cue_file, tracknumber = parser.parse_url(self.player.get_current_track())
            cue_sheet = parser.parse(cue_file)
            track = cue_sheet.tracks[int(tracknumber) - 1]
            self.ui.artist_label.setText(track.artist)
            self.ui.album_label.setText(cue_sheet.title)
            self.ui.title_label.setText(track.title)
            self.ui.seek_slider.setMaximum(track.duration * 1000 + track.timestamp * 1000)
            self.ui.seek_slider.setMinimum(track.timestamp * 1000)
            self.player.player.setPosition(track.timestamp * 1000)
            self.ui.total_time.setText(utils.ms_to_str(track.duration * 1000))
        else:
            self.ui.artist_label.setText(" & ".join(self.player.get_metadata().value(QMediaMetaData.Key.ContributingArtist)))
            self.ui.album_label.setText(self.player.get_metadata().value(QMediaMetaData.Key.AlbumTitle))
            self.ui.title_label.setText(self.player.get_metadata().value(QMediaMetaData.Key.Title))
            self.ui.seek_slider.setMinimum(0)
            self.ui.seek_slider.setMaximum(self.player.player.duration())
            self.ui.total_time.setText(utils.ms_to_str(self.player.player.duration()))
        self.ui.track_label.setText(F"{self.player.current_track+1}/{len(self.player.queue)}")
        self.change_thumbnail()
    
    def change_thumbnail(self):
        img = self.player.get_metadata().value(QMediaMetaData.Key.ThumbnailImage)
        if img is None:
            self.ui.central_widget.setStyleSheet("#queue_widget { background-image: url(cat.png); background-position: bottom left; background-repeat: no-repeat; background-attachment: fixed; }")
            return
        img.scaled(QSize(320, 320)).save("/tmp/bg.jpg")
        self.ui.central_widget.setStyleSheet("#queue_widget { background-image: url(/tmp/bg.jpg); background-position: bottom left; background-repeat: no-repeat; background-attachment: fixed; }")
    
    def toggle_play(self):
        if self.ui.play_button.icon().name() == QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart).name():
            self.ui.play_button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        else:
            self.ui.play_button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.player.toggle_play()
    
    def update_pos(self, pos):
        self.ui.seek_slider.setValue(pos)
        self.ui.curr_time.setText(utils.ms_to_str(pos - self.ui.seek_slider.minimum()))
    
    def update_vol(self, vol):
        self.player.output.setVolume(float(vol) / 100)
        self.ui.volume_percent.setText(F"{vol}%")
    
    def seeked(self, pos):
        self.player.player.setPosition(pos)
    
    def setup_queue(self):
        self.queue_setup = True
        for i in self.player.queue:
            if i.startswith("cue://"):
                cue_file, tracknumber = parser.parse_url(i)
                cue_sheet = parser.parse(cue_file)
                track = cue_sheet.tracks[int(tracknumber) - 1]
                item = QStandardItem(F"{track.artist} - {track.title}")
                item.setWhatsThis(i)
                self.ui.queue_model.appendRow(item)
            else:
                tags = taglib.File(i).tags
                item = QStandardItem(F"{" & ".join(tags["ARTIST"])} - {tags["TITLE"][0]}")
                item.setWhatsThis(i)
                self.ui.queue_model.appendRow(item)
        self.queue_setup = False
    
    def rearrange_queue(self, *args):
        if self.queue_setup:
            return
        new_queue = []
        for i in range(self.ui.queue_model.rowCount()):
            new_queue.append(self.ui.queue_model.item(i).whatsThis())
        new_current = new_queue.index(self.player.get_current_track())
        self.player.queue = new_queue
        self.player.current_track = new_current
    
    def setup_artists(self):
        self.ui.artists_model.clear()
        artists = db.get_artists()
        for a in artists:
            item = QStandardItem(a)
            item.setIcon(QIcon("artist.png"))
            item.setToolTip(a)
            self.ui.artists_model.appendRow(item)

    def setup_albums(self):
        self.ui.albums_model.clear()
        albums = db.get_albums()
        for a in albums:
            icon = QIcon("cat.png")
            # try: # TODO: figure out how to not block everything when first rendered
            #     cover = QByteArray(audio_metadata.load(db.get_track(a["artist"], a["album"])["filename"])["pictures"][0].data)
            #     pixmap = QPixmap()
            #     pixmap.loadFromData(cover)
            #     icon = QIcon(pixmap.scaled(QSize(200,200)))
            # except Exception:
            #     icon = QIcon("cat.png")
            item = QStandardItem(icon, F"{a["album"]} - {a["artist"]}")
            item.setToolTip(F"{a["artist"]} - {a["album"]}")
            self.ui.albums_model.appendRow(item)
    
    def setup_playlists(self):
        playlists_dir = Path(os.path.join(str(Path("~").expanduser()), ".config/quching/playlists"))
        playlists = glob.glob(F"{playlists_dir}/*.txt")
        for playlist in playlists:
            item = QStandardItem(QIcon("playlist.png"), Path(os.path.join(playlists_dir, playlist)).stem)
            item.setWhatsThis(str(os.path.join(playlists_dir, playlist)))
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.ui.playlists_model.appendRow(item)

    def setup_dynamic_playlists(self):
        playlists_dir = Path(os.path.join(str(Path("~").expanduser()), ".config/quching/dynamic_playlists"))
        playlists = glob.glob(F"{playlists_dir}/*.json")
        for playlist in playlists:
            item = QStandardItem(QIcon("playlist.png"), Path(os.path.join(playlists_dir, playlist)).stem)
            item.setWhatsThis(str(os.path.join(playlists_dir, playlist)))
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.ui.dynamic_playlists_model.appendRow(item)
    
    def setup_shortcuts(self):
        self.space = QShortcut(QKeySequence(Qt.Key.Key_Space), self)
        self.space.activated.connect(self.toggle_play)
        # self.media_play = QShortcut(QKeySequence(Qt.Key.Key_MediaTogglePlayPause), self)
        # self.media_play.activated.connect(self.toggle_play)
        # self.media_next = QShortcut(QKeySequence(Qt.Key.Key_MediaNext), self)
        # self.media_next.activated.connect(self.player.play_next)
        # self.media_previous = QShortcut(QKeySequence(Qt.Key.Key_MediaPrevious), self)
        # self.media_previous.activated.connect(self.player.play_previous)
    
    def display_artist(self, index):
        self.ui.artists_stacked_widget.setCurrentIndex(1)
        self.ui.albums_tree.clear()
        artist = index.data()
        albums = db.get_artist_albums(artist)
        for a in albums:
            tracks = db.get_album_tracks(artist, a["album"])
            item = QTreeWidgetItem(self.ui.albums_tree, a)
            item.setFirstColumnSpanned(True)
            try:
                cover = QByteArray(audio_metadata.load(tracks[0][0])["pictures"][0].data)
                pixmap = QPixmap()
                pixmap.loadFromData(cover)
                item.setIcon(0, QIcon(pixmap))
            except Exception:
                item.setIcon(0, QIcon("cat.png"))
            item.setToolTip(0, a[0])
            for t in tracks:
                if "cue" in t.keys():
                    tracknumber = item.childCount() + 1
                    track = QTreeWidgetItem(item, [F"{tracknumber}. {t["title"]}", utils.ms_to_str(int(t["duration"] * 1000))])
                    track.setWhatsThis(0, F"cue://{t["cue"]}/{tracknumber}")
                else:
                    track = QTreeWidgetItem(item, [F"{t["tracknumber"]}. {t["title"]}", utils.ms_to_str(int(t["duration"] * 1000))])
                    track.setWhatsThis(0, t["filename"])

    def display_album(self, index):
        self.ui.album_stacked_widgets.setCurrentIndex(1)
        self.ui.album_tracks.clear()
        album, artist = index.data().split(" - ")
        tracks = db.get_album_tracks(artist, album)
        try:
            filename = tracks[0]["filename"]
            if "cue" in tracks[0].keys():
                filename = os.path.join(os.path.dirname(tracks[0]["cue"]), tracks[0]["filename"])
            cover = QByteArray(audio_metadata.load(filename)["pictures"][0].data)
            pixmap = QPixmap()
            pixmap.loadFromData(cover)
            self.ui.cover_art.setPixmap(pixmap.scaled(QSize(200,200)))
        except Exception as e:
            print(e.args)
            self.ui.cover_art.setPixmap(QPixmap.fromImage(QImage("cat.png")))
        for idx, t in enumerate(tracks):
            if "cue" in t.keys():
                track = QTreeWidgetItem(self.ui.album_tracks, [F"{idx + 1}. {t["title"]}", utils.ms_to_str(int(t["duration"] * 1000))])
                track.setWhatsThis(0, F"cue://{t["cue"]}/{idx + 1}")
            else:
                track = QTreeWidgetItem(self.ui.album_tracks, [F"{t["tracknumber"]}. {t["title"]}", utils.ms_to_str(int(t["duration"] * 1000))])
                track.setWhatsThis(0, t["filename"])

    def display_playlist(self, index):
        self.ui.playlists_tab_widget.setCurrentIndex(1)
        self.ui.playlist_tracks.clear()
        item = self.ui.playlists_model.itemFromIndex(index)
        playlist = open(item.whatsThis(), "r").read().splitlines()
        for idx, line in enumerate(playlist):
            track = None
            icon = QIcon("cat.png")
            if line.startswith("cue://"):
                track_cue, tracknumber = parser.parse_url(line)
                cue_sheet = parser.parse(track_cue)
                cue_track = cue_sheet.tracks[int(tracknumber) - 1]
                track = QTreeWidgetItem(self.ui.playlist_tracks, ["", F"{idx + 1}. {cue_track.artist} - {cue_track.title}", utils.ms_to_str(int(cue_track.duration * 1000))])
                try:
                    cover = QByteArray(audio_metadata.load(os.path.join(os.path.dirname(cue_sheet.cue_file), cue_track.file))["pictures"][0].data)
                    pixmap = QPixmap()
                    pixmap.loadFromData(cover)
                    icon = QIcon(pixmap)
                except Exception:
                    icon = QIcon("cat.png")
            else:
                track_meta = taglib.File(line)
                track_tags = track_meta.tags
                track = QTreeWidgetItem(self.ui.playlist_tracks, ["", F"{idx + 1}. {" & ".join(track_tags["ARTIST"])} - {track_tags["TITLE"][0]}", utils.ms_to_str(int(track_meta.length * 1000))])
                try:
                    cover = QByteArray(audio_metadata.load(line)["pictures"][0].data)
                    pixmap = QPixmap()
                    pixmap.loadFromData(cover)
                    icon = QIcon(pixmap)
                except Exception:
                    icon = QIcon("cat.png")
            track.setWhatsThis(0, line)
            track.setIcon(0, icon)

    def display_dynamic_playlist(self, index):
        self.ui.playlists_tab_widget.setCurrentIndex(1)
        self.ui.playlist_tracks.clear()
        item = self.ui.dynamic_playlists_model.itemFromIndex(index)
        playlist_search = json.loads(open(item.whatsThis(), "r").read())
        playlist = db.search_db(playlist_search)
        for idx, line in enumerate(playlist):
            track = None
            icon = QIcon("cat.png")
            if "cue" in line.keys():
                track = QTreeWidgetItem(self.ui.playlist_tracks,
                                        ["", F"{idx + 1}. {line["artist"]} - {line["title"]}",
                                         utils.ms_to_str(int(line["duration"] * 1000))])
                track.setWhatsThis(0, F"cue://{line["cue"]}/{line["tracknumber"]}")
                try:
                    cover = QByteArray(
                        audio_metadata.load(os.path.join(os.path.dirname(line["cue_file"]), line["file"]))[
                            "pictures"][0].data)
                    pixmap = QPixmap()
                    pixmap.loadFromData(cover)
                    icon = QIcon(pixmap)
                except Exception:
                    icon = QIcon("cat.png")
            else:
                track_meta = taglib.File(line)
                track_tags = track_meta.tags
                track = QTreeWidgetItem(self.ui.playlist_tracks, ["",
                                                                  F"{idx + 1}. {" & ".join(track_tags["ARTIST"])} - {track_tags["TITLE"][0]}",
                                                                  utils.ms_to_str(int(track_meta.length * 1000))])
                track.setWhatsThis(0, line["filename"])
                try:
                    cover = QByteArray(audio_metadata.load(line)["pictures"][0].data)
                    pixmap = QPixmap()
                    pixmap.loadFromData(cover)
                    icon = QIcon(pixmap)
                except Exception:
                    icon = QIcon("cat.png")
            track.setIcon(0, icon)

    def back_to_artists(self):
        self.ui.artists_stacked_widget.setCurrentIndex(0)
    
    def back_to_albums(self):
        self.ui.album_stacked_widgets.setCurrentIndex(0)
    
    def back_to_playlists(self):
        self.ui.playlists_tab_widget.setCurrentIndex(0)
    
    def add_to_queue(self, item, column):
        if not self.player.queue:
            was_empty = True
        else:
            was_empty = False
        if item.childCount() != 0:
            for i in range(item.childCount()):
                self.add_to_queue(item.child(i), column)
            return
        file = item.whatsThis(0)
        self.player.queue.append(file)
        if file.startswith("cue://"):
            cue_file, tracknumber = parser.parse_url(file)
            cue_sheet = parser.parse(cue_file)
            track = cue_sheet.tracks[int(tracknumber) - 1]
            item = QStandardItem(F"{track.artist} - {track.title}")
            item.setWhatsThis(file)
            self.ui.queue_model.appendRow(item)
        else:
            tags = taglib.File(file).tags
            item = QStandardItem(F"{" & ".join(tags["ARTIST"])} - {tags["TITLE"][0]}")
            item.setWhatsThis(file)
            self.ui.queue_model.appendRow(item)
        if was_empty:
            self.player.player.setSource(file)
            self.ui.play_button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
            self.toggle_play()
    
    def toggle_shuffle(self, _):
        self.queue_setup = True
        self.player.toggle_shuffle()
        self.ui.queue_model.clear()
        self.setup_queue()
    
    def clear_queue(self, _):
        self.queue_setup = True
        self.player.queue = []
        self.player.current_track = -1
        self.ui.queue_model.clear()
        self.setup_queue()

    def compile_dynamic_playlist(self, file):
        playlist_selectors = json.loads(open(file).read())
        tracks = db.search_db(playlist_selectors, 50)  # TODO: lazy load the playlist instead of loading a whole chunk at once
        audio_tracks = [t["filename"] for t in tracks if "cue" not in t.keys()]
        cue_tracks = [F"cue://{t["cue"]}/{t["tracknumber"]}" for t in tracks if "cue" in t.keys()]
        return audio_tracks + cue_tracks
    
    def play_playlist(self, _):
        if self.ui.playlist_page_switcher.currentText() == "Dynamic":
            selection_model = self.ui.dynamic_playlists_list.selectionModel()
        else:
            selection_model = self.ui.playlists_list.selectionModel()
        if selection_model.hasSelection():
            if self.ui.playlist_page_switcher.currentText() == "Dynamic":
                playlist = self.ui.dynamic_playlists_model.itemFromIndex(selection_model.selectedIndexes()[0])
                playlist_tracks = self.compile_dynamic_playlist(playlist.whatsThis())
            else:
                playlist = self.ui.playlists_model.itemFromIndex(selection_model.selectedIndexes()[0])
                playlist_tracks = open(playlist.whatsThis(), "r").read().splitlines()
            self.clear_queue(_)
            self.player.queue = playlist_tracks
            self.player.current_track = -1
            self.setup_queue()
    
    def edit_playlist(self):
        if self.ui.playlist_page_switcher.currentIndex():
            selection_model = self.ui.dynamic_playlists_list.selectionModel()
        else:
            selection_model = self.ui.playlists_list.selectionModel()
        if selection_model.hasSelection():
            if self.ui.playlist_page_switcher.currentIndex():
                playlist = self.ui.dynamic_playlists_model.itemFromIndex(selection_model.selectedIndexes()[0])
                dialog = QuchingDynamicPlaylistWizard(playlist_file=playlist.whatsThis(), name=playlist.text())
                dialog.exec()
            else:
                playlist = self.ui.playlists_model.itemFromIndex(selection_model.selectedIndexes()[0])
                dialog = QuchingPlaylistComposer(playlist=playlist.whatsThis(), name=playlist.text())
                dialog.exec()

    def open_playlist_dialog(self, _):
        if self.ui.playlist_page_switcher.currentIndex():
            dialog = QuchingDynamicPlaylistWizard()
            dialog.exec()
        else:
            dialog = QuchingPlaylistComposer()
            dialog.exec()