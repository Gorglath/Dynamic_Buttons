import os
import six

from Qt import QtCompat, QtWidgets, QtCore

from engine import base_engine
from tool.ui import save_window as sw

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

main_ui_path = Path(__file__).parent / 'qt' / 'Window.ui'

UserRole = QtCore.Qt.UserRole


class ToolWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(main_ui_path), self)
        self.engine = base_engine.get_engine()
        # self.open_pb.clicked.connect(self.open_file)
        # self.save_pb.clicked.connect(self.save_file)
        # self.reference_pb.clicked.connect(self.reference_file)
        self.create_buttons()
        self.update_list()

    def create_buttons(self):
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QtWidgets.QVBoxLayout(self.centralwidget)

        self.list_lw = QtWidgets.QListWidget()
        self.lay.addWidget(self.list_lw)
        for implementation in self.engine.implements:
            button = QtWidgets.QPushButton(implementation)
            button.setToolTip(implementation)
            button.clicked.connect(self.assign_function(implementation))
            self.lay.addWidget(button)

        self.lay.addStretch(1)

    def assign_function(self, button_name):
        if 'Open' in button_name:
            return self.open_file
        elif 'Save' in button_name:
            return self.save_file
        else:
            return self.custom_function

    def update_list(self):
        for f in self.engine.get_files():
            add_list_widget_item(self.list_lw, f, os.path.basename(f))

    def open_file(self):
        item = self.list_lw.currentItem()
        path = item.data(UserRole)
        self.engine.open_file(path)
        self.close()

    def save_file(self):
        s = sw.SaveWindow(self.engine)
        s.show()

    def custom_function(self):
        item = self.list_lw.currentItem()
        path = item.data(UserRole)
        clicked_button = self.sender()
        name = clicked_button.text()
        self.engine.activate_function(name,path)


def add_list_widget_item(list_widget, data, label):
    """ Used to fill a UI listWidget with listWidgetItem (label + data) """
    item = QtWidgets.QListWidgetItem()
    item.setData(UserRole, data)
    item.setText(label)
    list_widget.addItem(item)
    return item


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()
