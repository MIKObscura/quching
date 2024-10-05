# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playlistkoHgJN.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_playlist_dialog(object):
    def setupUi(self, playlist_dialog):
        if not playlist_dialog.objectName():
            playlist_dialog.setObjectName(u"playlist_dialog")
        playlist_dialog.setEnabled(True)
        playlist_dialog.resize(640, 480)
        self.dialog_layout = QVBoxLayout(playlist_dialog)
        self.dialog_layout.setObjectName(u"dialog_layout")
        self.playlist_name_box = QLineEdit(playlist_dialog)
        self.playlist_name_box.setObjectName(u"playlist_name_box")
        self.playlist_name_box.setClearButtonEnabled(True)

        self.dialog_layout.addWidget(self.playlist_name_box)

        self.main_widget = QWidget(playlist_dialog)
        self.main_widget.setObjectName(u"main_widget")
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setObjectName(u"main_layout")
        self.playlist_composer_tabs = QTabWidget(self.main_widget)
        self.playlist_composer_tabs.setObjectName(u"playlist_composer_tabs")
        self.browser_tab = QWidget()
        self.browser_tab.setObjectName(u"browser_tab")
        self.browser_layout = QVBoxLayout(self.browser_tab)
        self.browser_layout.setObjectName(u"browser_layout")
        self.search_label = QLabel(self.browser_tab)
        self.search_label.setObjectName(u"search_label")

        self.browser_layout.addWidget(self.search_label)

        self.search_fields = QWidget(self.browser_tab)
        self.search_fields.setObjectName(u"search_fields")
        self.search_fields_layout = QVBoxLayout(self.search_fields)
        self.search_fields_layout.setObjectName(u"search_fields_layout")
        self.first_search = QWidget(self.search_fields)
        self.first_search.setObjectName(u"first_search")
        self.first_field_layout = QHBoxLayout(self.first_search)
        self.first_field_layout.setObjectName(u"first_field_layout")
        self.field_choice = QComboBox(self.first_search)
        self.field_choice.addItem("")
        self.field_choice.addItem("")
        self.field_choice.addItem("")
        self.field_choice.addItem("")
        self.field_choice.addItem("")
        self.field_choice.addItem("")
        self.field_choice.addItem("")
        self.field_choice.setObjectName(u"field_choice")

        self.first_field_layout.addWidget(self.field_choice)

        self.search_term = QLineEdit(self.first_search)
        self.search_term.setObjectName(u"search_term")

        self.first_field_layout.addWidget(self.search_term)


        self.search_fields_layout.addWidget(self.first_search)

        self.additional_search = QWidget(self.search_fields)
        self.additional_search.setObjectName(u"additional_search")
        self.additional_field_1_layout = QHBoxLayout(self.additional_search)
        self.additional_field_1_layout.setObjectName(u"additional_field_1_layout")

        self.search_fields_layout.addWidget(self.additional_search)


        self.browser_layout.addWidget(self.search_fields)

        self.tracks_table = QTableWidget(self.browser_tab)
        if (self.tracks_table.columnCount() < 5):
            self.tracks_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tracks_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tracks_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tracks_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tracks_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tracks_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tracks_table.setObjectName(u"tracks_table")
        self.tracks_table.setEnabled(True)
        self.tracks_table.setProperty("showDropIndicator", False)
        self.tracks_table.setDragDropOverwriteMode(False)
        self.tracks_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tracks_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tracks_table.setSortingEnabled(True)
        self.tracks_table.setRowCount(0)
        self.tracks_table.setColumnCount(5)
        self.tracks_table.horizontalHeader().setCascadingSectionResizes(True)
        self.tracks_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.tracks_table.horizontalHeader().setStretchLastSection(True)
        self.tracks_table.verticalHeader().setVisible(False)

        self.browser_layout.addWidget(self.tracks_table)

        self.playlist_composer_tabs.addTab(self.browser_tab, "")
        self.playlist_tab = QWidget()
        self.playlist_tab.setObjectName(u"playlist_tab")
        self.playlist_view_layout = QGridLayout(self.playlist_tab)
        self.playlist_view_layout.setObjectName(u"playlist_view_layout")
        self.playlist_view = QListWidget(self.playlist_tab)
        self.playlist_view.setObjectName(u"playlist_view")
        self.playlist_view.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

        self.playlist_view_layout.addWidget(self.playlist_view, 0, 0, 1, 1)

        self.playlist_composer_tabs.addTab(self.playlist_tab, "")

        self.main_layout.addWidget(self.playlist_composer_tabs)


        self.dialog_layout.addWidget(self.main_widget)

        self.end_buttonbox = QDialogButtonBox(playlist_dialog)
        self.end_buttonbox.setObjectName(u"end_buttonbox")
        self.end_buttonbox.setEnabled(False)
        self.end_buttonbox.setOrientation(Qt.Orientation.Horizontal)
        self.end_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.dialog_layout.addWidget(self.end_buttonbox)


        self.retranslateUi(playlist_dialog)
        self.end_buttonbox.accepted.connect(playlist_dialog.accept)
        self.end_buttonbox.rejected.connect(playlist_dialog.reject)

        self.playlist_composer_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(playlist_dialog)
    # setupUi

    def retranslateUi(self, playlist_dialog):
        playlist_dialog.setWindowTitle(QCoreApplication.translate("playlist_dialog", u"Dialog", None))
        self.playlist_name_box.setInputMask("")
        self.playlist_name_box.setText("")
        self.playlist_name_box.setPlaceholderText(QCoreApplication.translate("playlist_dialog", u"playlist name", None))
        self.search_label.setText(QCoreApplication.translate("playlist_dialog", u"Search Tracks", None))
        self.field_choice.setItemText(0, QCoreApplication.translate("playlist_dialog", u"artist", None))
        self.field_choice.setItemText(1, QCoreApplication.translate("playlist_dialog", u"album", None))
        self.field_choice.setItemText(2, QCoreApplication.translate("playlist_dialog", u"title", None))
        self.field_choice.setItemText(3, QCoreApplication.translate("playlist_dialog", u"year", None))
        self.field_choice.setItemText(4, QCoreApplication.translate("playlist_dialog", u"genre", None))
        self.field_choice.setItemText(5, QCoreApplication.translate("playlist_dialog", u"bitrate", None))
        self.field_choice.setItemText(6, QCoreApplication.translate("playlist_dialog", u"samplerate", None))

        self.field_choice.setPlaceholderText(QCoreApplication.translate("playlist_dialog", u"field", None))
        ___qtablewidgetitem = self.tracks_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("playlist_dialog", u"Artist", None));
        ___qtablewidgetitem1 = self.tracks_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("playlist_dialog", u"Album", None));
        ___qtablewidgetitem2 = self.tracks_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("playlist_dialog", u"Title", None));
        ___qtablewidgetitem3 = self.tracks_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("playlist_dialog", u"Year", None));
        ___qtablewidgetitem4 = self.tracks_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("playlist_dialog", u"Genre", None));
        self.playlist_composer_tabs.setTabText(self.playlist_composer_tabs.indexOf(self.browser_tab), QCoreApplication.translate("playlist_dialog", u"Browse Tracks", None))
        self.playlist_composer_tabs.setTabText(self.playlist_composer_tabs.indexOf(self.playlist_tab), QCoreApplication.translate("playlist_dialog", u"Playlist", None))
    # retranslateUi

