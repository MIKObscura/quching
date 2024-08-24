from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QSize, QByteArray)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem, QShortcut, QKeySequence)
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QListView, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QTabWidget, QToolButton, QListWidget,
    QWidget, QAbstractSlider, QAbstractItemView, QTreeWidget, QTreeWidgetItem)
from PySide6.QtMultimedia import QMediaMetaData, QMediaPlayer
import quching.utils as utils
import taglib
import audio_metadata
import quching.indexer.database as db

class QuchingUI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.queue_dock = QDockWidget(MainWindow)
        self.queue_dock.setObjectName(u"queue_dock")
        self.queue_dock.setFloating(False)
        self.queue_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.queue_dock_widget = QWidget()
        self.queue_dock_widget.setObjectName(u"queue_dock_widget")
        self.queue_dock.setStyleSheet("#queue_dock_widget { background-image: url(cat.png); background-position: bottom left; background-repeat: no-repeat }")
        self.queue_dock_widget.setStyleSheet("#queue_view { background-color: rgba(0,0,0,0%) } #queue_view::item { padding-top: 5px }")
        self.gridLayout_3 = QGridLayout(self.queue_dock_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.queue_view = QListView(self.queue_dock_widget)
        self.queue_view.setObjectName(u"queue_view")
        self.queue_model = QStandardItemModel()
        self.queue_view.setModel(self.queue_model)
        self.queue_view.setMovement(QListView.Movement.Snap)
        #self.queue_view.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.queue_view.setDragDropMode(QAbstractItemView.InternalMove)

        self.gridLayout_3.addWidget(self.queue_view, 0, 0, 1, 1)

        self.queue_dock.setWidget(self.queue_dock_widget)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.queue_dock)
        self.browser_dock = QDockWidget(MainWindow)
        self.browser_dock.setObjectName(u"browser_dock")
        self.browser_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.browser_dock.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.browser_dock_widget = QWidget()
        self.browser_dock_widget.setObjectName(u"browser_dock_widget")
        self.gridLayout_4 = QGridLayout(self.browser_dock_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.browser_tabs = QTabWidget(self.browser_dock_widget)
        self.browser_tabs.setObjectName(u"browser_tabs")
        self.artists_tab = QWidget()
        self.artists_tab.setObjectName(u"artists_tab")
        self.gridLayout_5 = QGridLayout(self.artists_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.artists_list = QListView(self.artists_tab)
        self.artists_list.setGridSize(QSize(100, 100))
        self.artists_list.setResizeMode(QListView.ResizeMode.Adjust)
        self.artists_model = QStandardItemModel()
        self.artists_list.setModel(self.artists_model)
        self.artists_list.setObjectName(u"artistsList")
        self.artists_list.setMovement(QListView.Movement.Static)
        self.artists_list.setFlow(QListView.Flow.LeftToRight)
        self.artists_list.setProperty("isWrapping", True)
        self.artists_list.setViewMode(QListView.ViewMode.IconMode)
        self.album_widget = QWidget(self.artists_tab)
        self.album_widget.setObjectName(u"album_widget")
        self.verticalLayout_2 = QVBoxLayout(self.album_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.backButton = QToolButton(self.album_widget)
        self.backButton.setObjectName(u"backButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.backButton.setIcon(icon)
        self.verticalLayout_2.addWidget(self.backButton)
        self.albumsTree = QTreeWidget(self.album_widget)
        self.albumsTree.setObjectName(u"albumsTree")
        self.albumsTree.setColumnCount(2)
        self.albumsTree.setHeaderLabels(["Title", "Duration"])
        self.verticalLayout_2.addWidget(self.albumsTree)
        self.gridLayout_5.addWidget(self.album_widget)
        self.album_widget.hide()

        self.gridLayout_5.addWidget(self.artists_list, 0, 0, 1, 1)

        self.browser_tabs.addTab(self.artists_tab, "")
        self.albums_tab = QWidget()
        self.albums_tab.setObjectName(u"albums_tab")
        self.gridLayout_6 = QGridLayout(self.albums_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tracklist_widget = QWidget(self.albums_tab)
        self.tracklist_widget.setObjectName(u"tracklist_widget")
        self.gridLayout_8 = QGridLayout(self.tracklist_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_6")
        self.album_tracks = QTreeWidget(self.tracklist_widget)
        self.album_tracks.setColumnCount(2)
        self.album_tracks.setHeaderLabels(["Title", "Duration"])
        self.album_tracks.setObjectName(u"album_tracks")
        self.gridLayout_8.addWidget(self.album_tracks, 2, 0, 1, 1)
        self.cover_art = QLabel(self.tracklist_widget)
        self.cover_art.setObjectName(u"cover_art")
        self.gridLayout_8.addWidget(self.cover_art, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        self.back_button2 = QToolButton(self.tracklist_widget)
        self.back_button2.setObjectName(u"back_button2")
        self.back_button2.setIcon(icon)
        self.gridLayout_8.addWidget(self.back_button2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.tracklist_widget, 1, 0, 1, 1)
        self.tracklist_widget.hide()

        self.albums_list = QListView(self.albums_tab)
        self.albums_list.setGridSize(QSize(100, 100))
        self.albums_list.setResizeMode(QListView.ResizeMode.Adjust)
        self.albums_model = QStandardItemModel()
        self.albums_list.setModel(self.albums_model)
        self.albums_list.setObjectName(u"albumsList")
        self.albums_list.setMovement(QListView.Movement.Static)
        self.albums_list.setFlow(QListView.Flow.LeftToRight)
        self.albums_list.setProperty("isWrapping", True)
        self.albums_list.setViewMode(QListView.ViewMode.IconMode)

        self.gridLayout_6.addWidget(self.albums_list, 0, 0, 1, 1)

        self.browser_tabs.addTab(self.albums_tab, "")
        self.playlists_tab = QWidget()
        self.playlists_tab.setObjectName(u"playlists_tab")
        self.gridLayout_7 = QGridLayout(self.playlists_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.playlistsList = QListView(self.playlists_tab)
        self.playlistsList.setObjectName(u"playlistsList")
        self.playlistsList.setMovement(QListView.Movement.Static)
        self.playlistsList.setFlow(QListView.Flow.LeftToRight)
        self.playlistsList.setProperty("isWrapping", True)
        self.playlistsList.setViewMode(QListView.ViewMode.IconMode)

        self.gridLayout_7.addWidget(self.playlistsList, 0, 0, 1, 1)

        self.browser_tabs.addTab(self.playlists_tab, "")

        self.gridLayout_4.addWidget(self.browser_tabs, 0, 0, 1, 1)

        self.browser_dock.setWidget(self.browser_dock_widget)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.browser_dock)
        self.controls_dock = QDockWidget(MainWindow)
        self.controls_dock.setObjectName(u"controls_dock")
        #self.controls_dock.setStyleSheet("#controls_dock_widget { background-image: url(cat.png); background-position: bottom center; background-repeat: no-repeat }")
        self.controls_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.controls_dock.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea|Qt.DockWidgetArea.TopDockWidgetArea)
        self.controls_dock_widget = QWidget()
        self.controls_dock_widget.setObjectName(u"controls_dock_widget")
        self.gridLayout = QGridLayout(self.controls_dock_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_button = QToolButton(self.controls_dock_widget)
        self.prev_button.setObjectName(u"prev_button")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward))
        self.prev_button.setIcon(icon)
        self.prev_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.prev_button)

        self.play_button = QToolButton(self.controls_dock_widget)
        self.play_button.setObjectName(u"play_button")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.play_button)

        self.next_button = QToolButton(self.controls_dock_widget)
        self.next_button.setObjectName(u"next_button")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.next_button.setIcon(icon2)
        self.next_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.next_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.curr_time = QLabel(self.controls_dock_widget)
        self.curr_time.setObjectName(u"curr_time")

        self.horizontalLayout.addWidget(self.curr_time)

        self.seek_slider = QSlider(self.controls_dock_widget)
        self.seek_slider.setObjectName(u"seek_slider")
        self.seek_slider.setOrientation(Qt.Orientation.Horizontal)
        self.seek_slider.setTracking(False)

        self.horizontalLayout.addWidget(self.seek_slider)

        self.total_time = QLabel(self.controls_dock_widget)
        self.total_time.setObjectName(u"total_time")

        self.horizontalLayout.addWidget(self.total_time)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.volume_percent = QLabel(self.controls_dock_widget)
        self.volume_percent.setObjectName(u"volume_percent")

        self.gridLayout.addWidget(self.volume_percent, 7, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.artistLabel = QLabel(self.controls_dock_widget)
        self.artistLabel.setObjectName(u"artistLabel")

        self.horizontalLayout_2.addWidget(self.artistLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.titleLabel = QLabel(self.controls_dock_widget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.horizontalLayout_2.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.albumLabel = QLabel(self.controls_dock_widget)
        self.albumLabel.setObjectName(u"albumLabel")

        self.horizontalLayout_2.addWidget(self.albumLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.trackLabel = QLabel(self.controls_dock_widget)
        self.trackLabel.setObjectName(u"yearLabel")

        self.horizontalLayout_2.addWidget(self.trackLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.volume_slider = QSlider(self.controls_dock_widget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volume_slider, 6, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.controls_dock.setWidget(self.controls_dock_widget)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.controls_dock)

        self.retranslateUi(MainWindow)

        self.browser_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quching", None))
        self.browser_tabs.setTabText(self.browser_tabs.indexOf(self.artists_tab), QCoreApplication.translate("MainWindow", u"Artists", None))
        self.browser_tabs.setTabText(self.browser_tabs.indexOf(self.albums_tab), QCoreApplication.translate("MainWindow", u"Albums", None))
        self.browser_tabs.setTabText(self.browser_tabs.indexOf(self.playlists_tab), QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.curr_time.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.total_time.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.volume_percent.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.artistLabel.setText(QCoreApplication.translate("MainWindow", u"%artist%", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"%title%", None))
        self.albumLabel.setText(QCoreApplication.translate("MainWindow", u"%album%", None))
        self.trackLabel.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
    # retranslateUi

class QuchingWindow(QMainWindow):
    def __init__(self, player, parent=None):
        super(QuchingWindow, self).__init__(parent)
        self.ui = QuchingUI()
        self.ui.setupUi(self)
        self.player = player
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
        self.ui.backButton.clicked.connect(self.back_to_artists)
        self.ui.back_button2.clicked.connect(self.back_to_albums)
        self.ui.albumsTree.itemDoubleClicked.connect(self.add_to_queue)
        self.ui.album_tracks.itemDoubleClicked.connect(self.add_to_queue)
        self.setup_tabs()
        self.setup_shortcuts()
        self.toggle_play()
    
    def load(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.change_meta()
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.play_next()
            self.player.player.play()
    
    def change_meta(self, media=None):
        if self.player.player.mediaStatus() != QMediaPlayer.MediaStatus.LoadedMedia:
            return
        self.ui.artistLabel.setText(" & ".join(self.player.get_metadata().value(QMediaMetaData.Key.ContributingArtist)))
        self.ui.albumLabel.setText(self.player.get_metadata().value(QMediaMetaData.Key.AlbumTitle))
        self.ui.titleLabel.setText(self.player.get_metadata().value(QMediaMetaData.Key.Title))
        self.ui.trackLabel.setText(F"{self.player.current_track+1}/{len(self.player.queue)}")
        self.ui.seek_slider.setMaximum(self.player.player.duration())
        self.ui.total_time.setText(utils.ms_to_str(self.player.player.duration()))
        self.change_thumbnail()
    
    def change_thumbnail(self):
        img = self.player.get_metadata().value(QMediaMetaData.Key.ThumbnailImage)
        if img is None:
            self.ui.queue_dock.setStyleSheet("#queue_dock_widget { background-image: url(cat.png); background-position: bottom left; background-repeat: no-repeat; background-attachment: fixed; }")
            return
        img.scaled(QSize(320, 320)).save("/tmp/bg.jpg")
        self.ui.queue_dock.setStyleSheet("#queue_dock_widget { background-image: url(/tmp/bg.jpg); background-position: bottom left; background-repeat: no-repeat; background-attachment: fixed; }")
    
    def toggle_play(self):
        if self.ui.play_button.icon().name() == QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart).name():
            self.ui.play_button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        else:
            self.ui.play_button.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.player.toggle_play()
    
    def update_pos(self, pos):
        self.ui.seek_slider.setValue(pos)
        self.ui.curr_time.setText(utils.ms_to_str(pos))
    
    def update_vol(self, vol):
        self.player.output.setVolume(float(vol) / 100)
        self.ui.volume_percent.setText(F"{vol}%")
    
    def seeked(self, pos):
        self.player.player.setPosition(pos)
    
    def setup_queue(self):
        for i in self.player.queue:
            tags = taglib.File(i).tags
            item = QStandardItem(F"{" & ".join(tags["ARTIST"])} - {tags["TITLE"][0]}")
            item.setWhatsThis(i)
            self.ui.queue_model.appendRow(item)
    
    def rearrange_queue(self, *args):
        new_queue = []
        for i in range(self.ui.queue_model.rowCount()):
            new_queue.append(self.ui.queue_model.item(i).whatsThis())
        new_current = new_queue.index(self.player.get_current_track())
        self.player.queue = new_queue
        self.player.current_track = new_current
    
    def setup_tabs(self):
        artists = db.get_artists()
        albums = db.get_albums()
        for a in artists:
            item = QStandardItem(a)
            item.setIcon(QIcon("artist.png"))
            item.setToolTip(a)
            self.ui.artists_model.appendRow(item)
        for a in albums:
            item = QStandardItem(F"{a[1]} - {a[0]}")
            item.setIcon(QIcon("cat.png"))
            item.setToolTip(F"{a[0]} - {a[1]}")
            self.ui.albums_model.appendRow(item)
    
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
        self.ui.artists_list.hide()
        self.ui.album_widget.show()
        self.ui.albumsTree.clear()
        artist = index.data()
        albums = db.get_artist_albums(artist)
        for a in albums:
            tracks = db.get_album_tracks(artist, a[0])
            item = QTreeWidgetItem(self.ui.albumsTree, a)
            item.setIcon(0, QIcon("cat.png"))
            item.setToolTip(0, a[0])
            for t in tracks:
                track = QTreeWidgetItem(item, [F"{t[3]}. {t[1]}", utils.ms_to_str(int(t[2] * 1000))])
                track.setWhatsThis(0, t[0])

    def display_album(self, index):
        self.ui.albums_list.hide()
        self.ui.tracklist_widget.show()
        self.ui.album_tracks.clear()
        album, artist = index.data().split(" - ")
        tracks = db.get_album_tracks(artist, album)
        try:
            cover = QByteArray(audio_metadata.load(tracks[0][0])["pictures"][0].data)
            pixmap = QPixmap()
            pixmap.loadFromData(cover)
            self.ui.cover_art.setPixmap(pixmap.scaled(QSize(200,200)))
        except Exception as e:
            print(e.args)
            self.ui.cover_art.setPixmap(QPixmap.fromImage(QImage("cat.png")))
        for t in tracks:
            track = QTreeWidgetItem(self.ui.album_tracks, [F"{t[3]}. {t[1]}", utils.ms_to_str(int(t[2] * 1000))])
            track.setWhatsThis(0, t[0])

    def back_to_artists(self):
        self.ui.album_widget.hide()
        self.ui.artists_list.show()
    
    def back_to_albums(self):
        self.ui.tracklist_widget.hide()
        self.ui.albums_list.show()
    
    def add_to_queue(self, item, column):
        file = item.whatsThis(0)
        self.player.queue.append(file)
        tags = taglib.File(file).tags
        item = QStandardItem(F"{" & ".join(tags["ARTIST"])} - {tags["TITLE"][0]}")
        item.setWhatsThis(file)
        self.ui.queue_model.appendRow(item)
