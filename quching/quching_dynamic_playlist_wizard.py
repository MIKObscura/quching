from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QComboBox, QDialog, QHBoxLayout, QLineEdit, QToolButton, QWidget, QTableWidgetItem)
from quching.gui.dynamic_playlist_dialog import Ui_dynamic_playlist
from quching.indexer.database import search_db
from quching.utils import str_to_s
import json
from pathlib import Path
import os

COLUMNS = ["artist", "album", "title", "year", "genre", "duration"]


class QuchingDynamicPlaylistWizard(QDialog):
    def __init__(self, window_type = Qt.WindowType.Dialog, playlist_file = None, name = None):
        super().__init__(None, window_type)
        self.ui = Ui_dynamic_playlist()
        self.ui.setupUi(self)
        self.fields = []
        self.name = ""
        if name is not None:
            self.name = name
            self.ui.playlist_name_box.setText(name)
        if playlist_file is not None:
            self.load_playlist(playlist_file)
        self.ui.add_field_button.clicked.connect(self.add_field)
        self.ui.preview_button.clicked.connect(self.preview)
        self.ui.end_button_box.accepted.connect(self.save_playlist)
        self.ui.playlist_name_box.textEdited.connect(self.toggle_dialog_buttons)

    def add_field(self):
        fields_amount = len(
            self.ui.fields_widget.findChildren(QWidget, options=Qt.FindChildOption.FindDirectChildrenOnly))
        new_field_widget = QWidget(self.ui.fields_widget)
        new_field_widget.setObjectName(F"field_widget{fields_amount}")
        field_layout = QHBoxLayout(new_field_widget)
        operator_selection = QComboBox(new_field_widget)
        operator_selection.setObjectName(F"operator_selection{fields_amount}")
        operator_selection.addItem("AND")
        operator_selection.addItem("OR")
        field_layout.addWidget(operator_selection)
        field_selection = QComboBox(new_field_widget)
        field_selection.setObjectName(F"field_selection{fields_amount}")
        field_selection.addItem("artist")
        field_selection.addItem("album")
        field_selection.addItem("year")
        field_selection.addItem("genre")
        field_selection.addItem("title")
        field_selection.addItem("duration")
        field_layout.addWidget(field_selection)
        equals_selection = QComboBox(new_field_widget)
        equals_selection.setObjectName(F"equals_selection{fields_amount}")
        equals_selection.addItem("=")
        equals_selection.addItem("!=")
        field_layout.addWidget(equals_selection)
        field_value = QLineEdit(new_field_widget)
        field_value.setObjectName(F"field_value{fields_amount}")
        field_layout.addWidget(field_value)
        remove_button = QToolButton(new_field_widget)
        remove_icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        remove_button.setIcon(remove_icon)
        remove_button.clicked.connect(self.remove_field)
        field_layout.addWidget(remove_button)
        self.ui.fields_layout.addWidget(new_field_widget)
        return operator_selection, field_selection, equals_selection, field_value

    def remove_field(self):
        sender = self.sender()
        if sender:
            sender.parentWidget().parentWidget().layout().removeWidget(sender.parentWidget())
            sender.parentWidget().deleteLater()

    def update_fields(self):
        field_lines = self.ui.fields_widget.findChildren(QWidget, options=Qt.FindChildOption.FindDirectChildrenOnly)
        selectors = []
        for field in field_lines:
            if field.objectName() == "first_field":
                query = self.ui.field_value.text()
                field_choice = self.ui.field_choice.currentText()
                equals_choice = self.ui.equals_choice.currentText()
                if len(query) == 0:
                    continue
                selectors.append((field_choice, equals_choice, query))
            else:
                selectors.extend(self.__get_selector_values(field, len(selectors)))
        self.fields = selectors

    def preview(self):
        self.update_fields()
        self.ui.preview_table.clearContents()
        query = search_db(self.fields, 20)
        row = 0
        for track in query:
            self.ui.preview_table.setRowCount(row + 1)
            for k in track.keys():
                if k not in COLUMNS:
                    continue
                item = QTableWidgetItem(track[k])
                if track[k] is not None and not isinstance(track[k], str):
                    item = QTableWidgetItem(str(track[k]))
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                column = COLUMNS.index(k)
                self.ui.preview_table.setItem(row, column, item)
            row += 1

    def __get_selector_values(self, field, field_num):
        query = field.findChild(QLineEdit).text()
        if len(query) == 0:
            return []
        field_selection = field.findChild(QComboBox, name=F"field_selection{field_num}").currentText()
        if field_selection == "year":
            query = int(query)
        if field_selection == "duration":
            query = str_to_s(query)
        operator_value = field.findChild(QComboBox, name=F"operator_selection{field_num}").currentText()
        equals_value = field.findChild(QComboBox, name=F"equals_selection{field_num}").currentText()
        return [operator_value, (field_selection, equals_value, query)]

    def toggle_dialog_buttons(self):
        self.update_fields()
        self.name = self.ui.playlist_name_box.text()
        if len(self.fields) == 0 or len(self.ui.playlist_name_box.text()) == 0:
            self.ui.end_button_box.setEnabled(False)
        else:
            self.ui.end_button_box.setEnabled(True)

    def load_playlist(self, file):
        playlist = json.loads(open(file).read())
        self.fields = playlist
        self.ui.field_value.setText(self.fields[0][2])
        self.ui.field_choice.setCurrentText(self.fields[0][0])
        self.ui.equals_choice.setCurrentText(self.fields[0][1])
        new_field = None
        for f in self.fields[1:]:
            if type(f) is str:
                new_field = self.add_field()
                new_field[0].setCurrentText(f)
            else:
                new_field[1].setCurrentText(f[0])
                new_field[2].setCurrentText(f[1])
                new_field[3].setText(f[2])

    def save_playlist(self):
        playlists_directory = Path(os.path.join(str(Path("~").expanduser()), ".config/quching/dynamic_playlists"))
        playlist_path = os.path.join(playlists_directory, F"{self.name}.json")
        playlist_file = open(playlist_path, "w")
        playlist_file.write(json.dumps(self.fields))
