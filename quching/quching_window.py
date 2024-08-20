from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QSize)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout,
    QLabel, QListView, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QTabWidget, QToolButton,
    QWidget, QAbstractSlider)
from PySide6.QtMultimedia import QMediaMetaData, QMediaPlayer
import quching.utils as utils

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
        self.queue_dock_widget.setStyleSheet("#queue_view { background-color: rgba(0,0,0,0%) }")
        self.gridLayout_3 = QGridLayout(self.queue_dock_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.queue_view = QListView(self.queue_dock_widget)
        self.queue_view.setObjectName(u"queue_view")
        self.queue_view.setMovement(QListView.Movement.Snap)

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
        self.browser_tabs.addTab(self.artists_tab, "")
        self.albums_tab = QWidget()
        self.albums_tab.setObjectName(u"albums_tab")
        self.browser_tabs.addTab(self.albums_tab, "")
        self.playlists_tab = QWidget()
        self.playlists_tab.setObjectName(u"playlists_tab")
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

        self.browser_tabs.setCurrentIndex(2)


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
        self.player.player.mediaStatusChanged.connect(self.load)
        self.ui.play_button.clicked.connect(self.toggle_play)
        self.player.player.sourceChanged.connect(self.change_meta)
        self.player.player.positionChanged.connect(self.update_pos)
        self.ui.seek_slider.sliderMoved.connect(self.seeked)
        self.ui.volume_slider.valueChanged.connect(self.update_vol)
        self.ui.volume_slider.setValue(int(self.player.output.volume() * 100))
        self.ui.volume_percent.setText(F"{self.ui.volume_slider.value()}%")
        self.toggle_play()
    
    def load(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self.change_meta()
    
    def change_meta(self):
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
        img.scaled(QSize(200, 200)).save("/tmp/bg.jpg")
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