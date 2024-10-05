from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
                               QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit, QListView,
                               QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
                               QToolButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QMenu)
import quching.indexer.database as db
from quching.gui.playlist_dialog import Ui_playlist_dialog
from quching.cue import parser
import taglib
from pathlib import Path
import os

COLUMNS = ["artist", "album", "title", "year", "genre", "duration"]

class QuchingPlaylistComposer(QDialog):
    def __init__(self, window_type = Qt.WindowType.Dialog, playlist = None, name = None):
        super(QuchingPlaylistComposer, self).__init__(None, window_type)
        self.ui = Ui_playlist_dialog()
        self.ui.setupUi(self)
        self.ui.playlist_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.playlist_context_menu = QMenu()
        search_icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.ui.search_action = self.ui.search_term.addAction(search_icon, QLineEdit.ActionPosition.LeadingPosition)
        self.ui.remove_action = self.ui.playlist_context_menu.addAction("Remove from playlist")
        self.playlist = []
        self.is_editing = False
        self.ui_setup = False
        self.current_index = None
        self.indexes = {
            "artist": None,
            "album": None,
            "title": None
        }
        if name is not None:
            self.name = name
            self.ui.playlist_name_box.setText(name)
        if playlist is not None:
            playlist_file = open(playlist, "r").read()
            self.playlist = playlist_file.splitlines()
            self.is_editing = True
            self.setup_playlist()
            self.ui.end_buttonbox.setEnabled(True)
        self.ui.playlist_name_box.textEdited.connect(self.toggle_dialog_buttons)
        self.ui.tracks_table.cellDoubleClicked.connect(self.add_to_playlist)
        self.ui.end_buttonbox.accepted.connect(self.save_playlist)
        self.ui.field_choice.currentTextChanged.connect(self.change_index)
        self.ui.search_action.triggered.connect(self.search)
        self.ui.playlist_view.model().rowsMoved.connect(self.reorder_playlist)
        self.ui.playlist_view.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.remove_action.triggered.connect(self.remove_from_playlist)
        self.setup_table()
    
    def setup_table(self):
        self.ui.tracks_table.setSortingEnabled(False)
        tracks = [*db.get_all_tracks(), *db.get_all_cue_tracks()]
        row = 0
        for t in tracks:
            self.ui.tracks_table.setRowCount(row + 1)
            whats_this = t["filename"]
            if "cue" in t.keys():
                whats_this = F"cue://{t['cue']}/{t['tracknumber']}"
            for k in t.keys():
                if k not in COLUMNS:
                    continue
                item = QTableWidgetItem(t[k])
                if t[k] is not None and not isinstance(t[k], str):
                    item = QTableWidgetItem(str(t[k]))
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                item.setWhatsThis(whats_this)
                column = COLUMNS.index(k)
                self.ui.tracks_table.setItem(row, column, item)
            row += 1
        self.ui.tracks_table.setSortingEnabled(True)
        first_artist, first_album, first_title = self.ui.tracks_table.item(0, 0), self.ui.tracks_table.item(0, 1), self.ui.tracks_table.item(0, 2)
        self.indexes["artist"] = self.ui.tracks_table.indexFromItem(first_artist)
        self.indexes["album"] = self.ui.tracks_table.indexFromItem(first_album)
        self.indexes["title"] = self.ui.tracks_table.indexFromItem(first_title)
        self.current_index = self.indexes["artist"]
    
    def setup_playlist(self):
        self.ui_setup = True
        for t in self.playlist:
            item = QListWidgetItem()
            item.setWhatsThis(t)
            if t.startswith("cue://"):
                cue_file, tracknumber = parser.parse_url(t)
                cue = parser.parse(cue_file)
                track = cue.tracks[int(tracknumber) - 1]
                item.setText(F"{track.artist} - {track.title}")
            else:
                tags = taglib.File(t).tags
                item.setText(F"{" & ".join(tags["ARTIST"])} - {tags["TITLE"][0]}")
            self.ui.playlist_view.insertItem(self.ui.playlist_view.count(), item)
        self.ui_setup = False

    def toggle_dialog_buttons(self, text):
        if self.ui.playlist_view.count() == 0 or len(self.ui.playlist_name_box.text()) == 0:
            self.ui.end_buttonbox.setEnabled(False)
        else:
            self.ui.end_buttonbox.setEnabled(True)
        self.name = text
    
    def add_to_playlist(self, row, column):
        artist = self.ui.tracks_table.item(row, COLUMNS.index("artist"))
        title = self.ui.tracks_table.item(row, COLUMNS.index("title"))
        item = QListWidgetItem()
        item.setText(F"{artist.text()} - {title.text()}")
        item.setWhatsThis(artist.whatsThis())
        self.playlist.append(artist.whatsThis())
        self.ui.playlist_view.insertItem(self.ui.playlist_view.count(), item)
    
    def save_playlist(self):
        playlists_directory = Path(os.path.join(str(Path("~").expanduser()), ".config/quching/playlists"))
        playlist_path = os.path.join(playlists_directory, F"{self.name}.txt")
        playlist_content = "\n".join(self.playlist)
        playlist_file = open(playlist_path, "w")
        playlist_file.write(playlist_content)

    def change_index(self, text):
        self.current_index = self.indexes[text]
    
    def search(self):
        start_item = self.ui.tracks_table.item(self.current_index.row() + 1, self.current_index.column())
        start_index = self.ui.tracks_table.indexFromItem(start_item)
        matches = self.ui.tracks_table.model().match(start_index, Qt.ItemDataRole.DisplayRole, self.ui.search_term.text())
        if len(matches) == 0:
            return
        index_matched = matches[0]
        self.current_index = index_matched
        self.indexes[self.ui.field_choice.currentText()] = index_matched
        self.ui.tracks_table.setCurrentIndex(index_matched)

    def reorder_playlist(self, *args):
        if self.ui_setup:
            return
        new_playlist = []
        for i in range(self.ui.playlist_view.count()):
            new_playlist.append(self.ui.playlist_view.item(i).whatsThis())
        self.playlist = new_playlist

    def show_context_menu(self, point):
        self.ui.playlist_context_menu.exec(self.ui.playlist_view.mapToGlobal(point))

    def remove_from_playlist(self):
        row = self.ui.playlist_view.currentRow()
        self.playlist.pop(row)
        self.ui.playlist_view.clear()
        self.setup_playlist()