# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dyn_playlistBbGATj.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QHeaderView, QLineEdit,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

COLUMNS = ["artist", "album", "title", "year", "genre", "duration"]

class QuchingDynamicPlaylistWizardUI(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.playlist_name_box = QLineEdit(Dialog)
        self.playlist_name_box.setObjectName(u"playlist_name_box")

        self.verticalLayout.addWidget(self.playlist_name_box)

        self.buttons_widget = QWidget(Dialog)
        self.buttons_widget.setObjectName(u"buttons_widget")
        self.horizontalLayout = QHBoxLayout(self.buttons_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.button_spacer)

        self.add_field_button = QToolButton(self.buttons_widget)
        self.add_field_button.setObjectName(u"add_field_button")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_field_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.add_field_button)

        self.remove_field_button = QToolButton(self.buttons_widget)
        self.remove_field_button.setObjectName(u"remove_field_button")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.remove_field_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.remove_field_button)

        self.clear_fields_button = QToolButton(self.buttons_widget)
        self.clear_fields_button.setObjectName(u"clear_fields_button")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.clear_fields_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.clear_fields_button)


        self.verticalLayout.addWidget(self.buttons_widget)

        self.fields_widget = QWidget(Dialog)
        self.fields_widget.setObjectName(u"fields_widget")
        self.verticalLayout_2 = QVBoxLayout(self.fields_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.first_field = QWidget(self.fields_widget)
        self.first_field.setObjectName(u"first_field")
        self.horizontalLayout_2 = QHBoxLayout(self.first_field)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.field_choice = QComboBox(self.first_field)
        self.field_choice.setObjectName(u"field_choice")

        self.horizontalLayout_2.addWidget(self.field_choice)

        self.field_value = QLineEdit(self.first_field)
        self.field_value.setObjectName(u"field_value")

        self.horizontalLayout_2.addWidget(self.field_value)


        self.verticalLayout_2.addWidget(self.first_field)


        self.verticalLayout.addWidget(self.fields_widget)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.preview_button = QToolButton(self.widget)
        self.preview_button.setObjectName(u"preview_button")
        self.preview_button.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.preview_button)


        self.verticalLayout.addWidget(self.widget)

        self.preview_table = QTableWidget(Dialog)
        self.preview_table.setObjectName(u"preview_table")
        self.preview_table.setColumnCount(6)
        for i, c in enumerate(COLUMNS):
            self.preview_table.setHorizontalHeaderItem(i, QTableWidgetItem(c))

        self.verticalLayout.addWidget(self.preview_table)

        self.end_button_box = QDialogButtonBox(Dialog)
        self.end_button_box.setObjectName(u"end_button_box")
        self.end_button_box.setOrientation(Qt.Orientation.Horizontal)
        self.end_button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.end_button_box.setEnabled(False)

        self.verticalLayout.addWidget(self.end_button_box)


        self.retranslateUi(Dialog)
        self.end_button_box.accepted.connect(Dialog.accept)
        self.end_button_box.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.playlist_name_box.setPlaceholderText(QCoreApplication.translate("Dialog", u"playlist name", None))
        self.add_field_button.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.remove_field_button.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.clear_fields_button.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.preview_button.setText(QCoreApplication.translate("Dialog", u"Preview", None))
    # retranslateUi

class QuchingDynamicPlaylistWizard(QDialog):
    def __init__(self, window_type = Qt.WindowType.Dialog, playlist_file = None, name = None):
        super().__init__(None, window_type)
        self.ui = QuchingDynamicPlaylistWizardUI()
        self.ui.setupUi(self)

