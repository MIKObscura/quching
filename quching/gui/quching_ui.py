# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quchingViUMQt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDockWidget,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListView, QMainWindow, QMenuBar, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Quching(object):
    def setupUi(self, Quching):
        if not Quching.objectName():
            Quching.setObjectName(u"Quching")
        Quching.resize(800, 600)
        self.central_widget = QWidget(Quching)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget_layout = QHBoxLayout(self.central_widget)
        self.central_widget_layout.setObjectName(u"central_widget_layout")
        self.queue_widget = QWidget(self.central_widget)
        self.queue_widget.setObjectName(u"queue_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queue_widget.sizePolicy().hasHeightForWidth())
        self.queue_widget.setSizePolicy(sizePolicy)
        self.queue_widget_layout = QVBoxLayout(self.queue_widget)
        self.queue_widget_layout.setObjectName(u"queue_widget_layout")
        self.queue_controls = QWidget(self.queue_widget)
        self.queue_controls.setObjectName(u"queue_controls")
        self.horizontalLayout_3 = QHBoxLayout(self.queue_controls)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clear_button = QToolButton(self.queue_controls)
        self.clear_button.setObjectName(u"clear_button")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.clear_button.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.clear_button)

        self.repeat_button = QToolButton(self.queue_controls)
        self.repeat_button.setObjectName(u"repeat_button")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistRepeat))
        self.repeat_button.setIcon(icon1)
        self.repeat_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.repeat_button)

        self.shuffle_button = QToolButton(self.queue_controls)
        self.shuffle_button.setObjectName(u"shuffle_button")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.shuffle_button.setIcon(icon2)
        self.shuffle_button.setCheckable(True)
        self.shuffle_button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.shuffle_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.queue_widget_layout.addWidget(self.queue_controls)

        self.queue_view = QListView(self.queue_widget)
        self.queue_view.setObjectName(u"queue_view")
        self.queue_view.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.queue_view.setMovement(QListView.Movement.Snap)

        self.queue_widget_layout.addWidget(self.queue_view)


        self.central_widget_layout.addWidget(self.queue_widget)

        self.browser_tabs = QTabWidget(self.central_widget)
        self.browser_tabs.setObjectName(u"browser_tabs")
        self.artists_tab = QWidget()
        self.artists_tab.setObjectName(u"artists_tab")
        self.artists_tab_layout = QVBoxLayout(self.artists_tab)
        self.artists_tab_layout.setObjectName(u"artists_tab_layout")
        self.artists_stacked_widget = QStackedWidget(self.artists_tab)
        self.artists_stacked_widget.setObjectName(u"artists_stacked_widget")
        self.artists_page = QWidget()
        self.artists_page.setObjectName(u"artists_page")
        self.artists_page_layout = QVBoxLayout(self.artists_page)
        self.artists_page_layout.setObjectName(u"artists_page_layout")
        self.artists_list = QListView(self.artists_page)
        self.artists_list.setObjectName(u"artists_list")
        self.artists_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.artists_list.setIconSize(QSize(150, 150))
        self.artists_list.setGridSize(QSize(150, 150))
        self.artists_list.setViewMode(QListView.ViewMode.IconMode)

        self.artists_page_layout.addWidget(self.artists_list)

        self.artists_stacked_widget.addWidget(self.artists_page)
        self.albums_page = QWidget()
        self.albums_page.setObjectName(u"albums_page")
        self.albums_page_layout = QVBoxLayout(self.albums_page)
        self.albums_page_layout.setObjectName(u"albums_page_layout")
        self.back_button3 = QToolButton(self.albums_page)
        self.back_button3.setObjectName(u"back_button3")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.back_button3.setIcon(icon3)

        self.albums_page_layout.addWidget(self.back_button3)

        self.albums_tree = QTreeWidget(self.albums_page)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(2, u"3");
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.albums_tree.setHeaderItem(__qtreewidgetitem)
        self.albums_tree.setObjectName(u"albums_tree")
        self.albums_tree.setIconSize(QSize(100, 100))
        self.albums_tree.setHeaderHidden(True)
        self.albums_tree.setColumnCount(3)

        self.albums_page_layout.addWidget(self.albums_tree)

        self.artists_stacked_widget.addWidget(self.albums_page)

        self.artists_tab_layout.addWidget(self.artists_stacked_widget)

        self.browser_tabs.addTab(self.artists_tab, "")
        self.albums_tab = QWidget()
        self.albums_tab.setObjectName(u"albums_tab")
        self.albums_tab_layout = QGridLayout(self.albums_tab)
        self.albums_tab_layout.setObjectName(u"albums_tab_layout")
        self.album_stacked_widgets = QStackedWidget(self.albums_tab)
        self.album_stacked_widgets.setObjectName(u"album_stacked_widgets")
        self.albums_list_page = QWidget()
        self.albums_list_page.setObjectName(u"albums_list_page")
        self.albums_list_layout = QVBoxLayout(self.albums_list_page)
        self.albums_list_layout.setObjectName(u"albums_list_layout")
        self.albums_list = QListView(self.albums_list_page)
        self.albums_list.setObjectName(u"albums_list")
        self.albums_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.albums_list.setIconSize(QSize(150, 150))
        self.albums_list.setGridSize(QSize(200, 200))
        self.albums_list.setViewMode(QListView.ViewMode.IconMode)

        self.albums_list_layout.addWidget(self.albums_list)

        self.album_stacked_widgets.addWidget(self.albums_list_page)
        self.tracklist_page = QWidget()
        self.tracklist_page.setObjectName(u"tracklist_page")
        self.album_tracklists_layout = QGridLayout(self.tracklist_page)
        self.album_tracklists_layout.setObjectName(u"album_tracklists_layout")
        self.cover_art = QLabel(self.tracklist_page)
        self.cover_art.setObjectName(u"cover_art")

        self.album_tracklists_layout.addWidget(self.cover_art, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.back_button2 = QToolButton(self.tracklist_page)
        self.back_button2.setObjectName(u"back_button2")
        self.back_button2.setIcon(icon3)

        self.album_tracklists_layout.addWidget(self.back_button2, 0, 0, 1, 1)

        self.album_tracks = QTreeWidget(self.tracklist_page)
        self.album_tracks.setObjectName(u"album_tracks")
        self.album_tracks.setColumnCount(2)

        self.album_tracklists_layout.addWidget(self.album_tracks, 2, 0, 1, 1)

        self.album_stacked_widgets.addWidget(self.tracklist_page)

        self.albums_tab_layout.addWidget(self.album_stacked_widgets, 1, 0, 1, 1)

        self.browser_tabs.addTab(self.albums_tab, "")
        self.playlists_tab = QWidget()
        self.playlists_tab.setObjectName(u"playlists_tab")
        self.playlists_tab_layout = QVBoxLayout(self.playlists_tab)
        self.playlists_tab_layout.setObjectName(u"playlists_tab_layout")
        self.playlists_tab_widget = QStackedWidget(self.playlists_tab)
        self.playlists_tab_widget.setObjectName(u"playlists_tab_widget")
        self.playlists_list_page = QWidget()
        self.playlists_list_page.setObjectName(u"playlists_list_page")
        self.playlists_list_layout = QVBoxLayout(self.playlists_list_page)
        self.playlists_list_layout.setObjectName(u"playlists_list_layout")
        self.playlist_edit = QWidget(self.playlists_list_page)
        self.playlist_edit.setObjectName(u"playlist_edit")
        self.playlist_edit_layout = QHBoxLayout(self.playlist_edit)
        self.playlist_edit_layout.setObjectName(u"playlist_edit_layout")
        self.play_playlist_button = QToolButton(self.playlist_edit)
        self.play_playlist_button.setObjectName(u"play_playlist_button")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.play_playlist_button.setIcon(icon4)

        self.playlist_edit_layout.addWidget(self.play_playlist_button)

        self.new_playlist_button = QToolButton(self.playlist_edit)
        self.new_playlist_button.setObjectName(u"new_playlist_button")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.new_playlist_button.setIcon(icon5)

        self.playlist_edit_layout.addWidget(self.new_playlist_button)

        self.edit_playlist_button = QToolButton(self.playlist_edit)
        self.edit_playlist_button.setObjectName(u"edit_playlist_button")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentPageSetup))
        self.edit_playlist_button.setIcon(icon6)

        self.playlist_edit_layout.addWidget(self.edit_playlist_button)

        self.delete_playlist_button = QToolButton(self.playlist_edit)
        self.delete_playlist_button.setObjectName(u"delete_playlist_button")
        self.delete_playlist_button.setIcon(icon)

        self.playlist_edit_layout.addWidget(self.delete_playlist_button)

        self.playlist_page_switcher = QComboBox(self.playlist_edit)
        self.playlist_page_switcher.addItem("")
        self.playlist_page_switcher.addItem("")
        self.playlist_page_switcher.setObjectName(u"playlist_page_switcher")

        self.playlist_edit_layout.addWidget(self.playlist_page_switcher)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.playlist_edit_layout.addItem(self.horizontalSpacer)


        self.playlists_list_layout.addWidget(self.playlist_edit)

        self.stacked_playlists_lists = QStackedWidget(self.playlists_list_page)
        self.stacked_playlists_lists.setObjectName(u"stacked_playlists_lists")
        self.playlists_page = QWidget()
        self.playlists_page.setObjectName(u"playlists_page")
        self.playlists_page_layout = QVBoxLayout(self.playlists_page)
        self.playlists_page_layout.setObjectName(u"playlists_page_layout")
        self.playlists_list = QListView(self.playlists_page)
        self.playlists_list.setObjectName(u"playlists_list")
        self.playlists_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.playlists_list.setIconSize(QSize(100, 100))
        self.playlists_list.setMovement(QListView.Movement.Static)
        self.playlists_list.setGridSize(QSize(150, 150))
        self.playlists_list.setViewMode(QListView.ViewMode.IconMode)

        self.playlists_page_layout.addWidget(self.playlists_list)

        self.stacked_playlists_lists.addWidget(self.playlists_page)
        self.dynamic_playlists_page = QWidget()
        self.dynamic_playlists_page.setObjectName(u"dynamic_playlists_page")
        self.dynamic_playlists_layout = QVBoxLayout(self.dynamic_playlists_page)
        self.dynamic_playlists_layout.setObjectName(u"dynamic_playlists_layout")
        self.dynamic_playlists_list = QListView(self.dynamic_playlists_page)
        self.dynamic_playlists_list.setObjectName(u"dynamic_playlists_list")
        self.dynamic_playlists_list.setIconSize(QSize(100, 100))
        self.dynamic_playlists_list.setGridSize(QSize(150, 150))
        self.dynamic_playlists_list.setViewMode(QListView.ViewMode.IconMode)

        self.dynamic_playlists_layout.addWidget(self.dynamic_playlists_list)

        self.stacked_playlists_lists.addWidget(self.dynamic_playlists_page)

        self.playlists_list_layout.addWidget(self.stacked_playlists_lists)

        self.playlists_tab_widget.addWidget(self.playlists_list_page)
        self.playlist_view = QWidget()
        self.playlist_view.setObjectName(u"playlist_view")
        self.playlist_view_layout = QVBoxLayout(self.playlist_view)
        self.playlist_view_layout.setObjectName(u"playlist_view_layout")
        self.back_button = QToolButton(self.playlist_view)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setIcon(icon3)

        self.playlist_view_layout.addWidget(self.back_button)

        self.playlist_tracks = QTreeWidget(self.playlist_view)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"Title");
        self.playlist_tracks.setHeaderItem(__qtreewidgetitem1)
        self.playlist_tracks.setObjectName(u"playlist_tracks")
        self.playlist_tracks.setIconSize(QSize(100, 100))

        self.playlist_view_layout.addWidget(self.playlist_tracks)

        self.playlists_tab_widget.addWidget(self.playlist_view)

        self.playlists_tab_layout.addWidget(self.playlists_tab_widget)

        self.browser_tabs.addTab(self.playlists_tab, "")

        self.central_widget_layout.addWidget(self.browser_tabs)

        Quching.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(Quching)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        Quching.setMenuBar(self.menubar)
        self.controls_dock = QDockWidget(Quching)
        self.controls_dock.setObjectName(u"controls_dock")
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
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward))
        self.prev_button.setIcon(icon7)
        self.prev_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.prev_button)

        self.play_button = QToolButton(self.controls_dock_widget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setIcon(icon4)
        self.play_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.play_button)

        self.next_button = QToolButton(self.controls_dock_widget)
        self.next_button.setObjectName(u"next_button")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.next_button.setIcon(icon8)
        self.next_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.next_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.curr_time = QLabel(self.controls_dock_widget)
        self.curr_time.setObjectName(u"curr_time")

        self.horizontalLayout.addWidget(self.curr_time)

        self.seek_slider = QSlider(self.controls_dock_widget)
        self.seek_slider.setObjectName(u"seek_slider")
        self.seek_slider.setOrientation(Qt.Orientation.Horizontal)

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
        self.artist_label = QLabel(self.controls_dock_widget)
        self.artist_label.setObjectName(u"artist_label")

        self.horizontalLayout_2.addWidget(self.artist_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.title_label = QLabel(self.controls_dock_widget)
        self.title_label.setObjectName(u"title_label")

        self.horizontalLayout_2.addWidget(self.title_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.album_label = QLabel(self.controls_dock_widget)
        self.album_label.setObjectName(u"album_label")

        self.horizontalLayout_2.addWidget(self.album_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.track_label = QLabel(self.controls_dock_widget)
        self.track_label.setObjectName(u"track_label")

        self.horizontalLayout_2.addWidget(self.track_label, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.volume_slider = QSlider(self.controls_dock_widget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volume_slider, 6, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.controls_dock.setWidget(self.controls_dock_widget)
        Quching.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.controls_dock)

        self.retranslateUi(Quching)

        self.browser_tabs.setCurrentIndex(0)
        self.artists_stacked_widget.setCurrentIndex(0)
        self.album_stacked_widgets.setCurrentIndex(0)
        self.playlists_tab_widget.setCurrentIndex(0)
        self.stacked_playlists_lists.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Quching)
    # setupUi

    def retranslateUi(self, Quching):
        Quching.setWindowTitle(QCoreApplication.translate("Quching", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.clear_button.setToolTip(QCoreApplication.translate("Quching", u"clear queue", None))
#endif // QT_CONFIG(tooltip)
        self.clear_button.setText(QCoreApplication.translate("Quching", u"...", None))
#if QT_CONFIG(tooltip)
        self.repeat_button.setToolTip(QCoreApplication.translate("Quching", u"repeat track", None))
#endif // QT_CONFIG(tooltip)
        self.repeat_button.setText(QCoreApplication.translate("Quching", u"...", None))
#if QT_CONFIG(tooltip)
        self.shuffle_button.setToolTip(QCoreApplication.translate("Quching", u"shuffle queue", None))
#endif // QT_CONFIG(tooltip)
        self.shuffle_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.back_button3.setText(QCoreApplication.translate("Quching", u"...", None))
        self.browser_tabs.setTabText(self.browser_tabs.indexOf(self.artists_tab), QCoreApplication.translate("Quching", u"Artists", None))
        self.cover_art.setText(QCoreApplication.translate("Quching", u"coverArt", None))
        self.back_button2.setText(QCoreApplication.translate("Quching", u"...", None))
        ___qtreewidgetitem = self.album_tracks.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Quching", u"Duration", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Quching", u"Title", None));
        self.browser_tabs.setTabText(self.browser_tabs.indexOf(self.albums_tab), QCoreApplication.translate("Quching", u"Albums", None))
        self.play_playlist_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.new_playlist_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.edit_playlist_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.delete_playlist_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.playlist_page_switcher.setItemText(0, QCoreApplication.translate("Quching", u"Standard", None))
        self.playlist_page_switcher.setItemText(1, QCoreApplication.translate("Quching", u"Dynamic", None))

        self.back_button.setText(QCoreApplication.translate("Quching", u"...", None))
        ___qtreewidgetitem1 = self.playlist_tracks.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Quching", u"Duration", None));
        self.browser_tabs.setTabText(self.browser_tabs.indexOf(self.playlists_tab), QCoreApplication.translate("Quching", u"Playlists", None))
        self.prev_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.play_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.next_button.setText(QCoreApplication.translate("Quching", u"...", None))
        self.curr_time.setText(QCoreApplication.translate("Quching", u"0:00", None))
        self.total_time.setText(QCoreApplication.translate("Quching", u"0:00", None))
        self.volume_percent.setText(QCoreApplication.translate("Quching", u"0%", None))
        self.artist_label.setText(QCoreApplication.translate("Quching", u"%artist%", None))
        self.title_label.setText(QCoreApplication.translate("Quching", u"%title%", None))
        self.album_label.setText(QCoreApplication.translate("Quching", u"%album%", None))
        self.track_label.setText(QCoreApplication.translate("Quching", u"0/0", None))
    # retranslateUi

