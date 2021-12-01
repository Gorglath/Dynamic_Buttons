import os
import six

from Qt import QtCompat, QtWidgets, QtCore

from engine import base_engine

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

save_ui_path = Path(__file__).parent / 'qt' / 'save_pop.ui'


class SaveWindow(QtWidgets.QMainWindow):

    def __init__(self, engine):
        super(SaveWindow, self).__init__()
        QtCompat.loadUi(str(save_ui_path), self)
        self.engine = engine;
        self.file_name_le.setText(self.engine.get_file_name())
        for f in self.engine.get_file_types():
            self.file_type_cb.addItem(f)
        self.file_save_pb.clicked.connect(self.finish_save_file)

    def finish_save_file(self):
        type = self.file_type_cb.currentText()
        name = self.file_name_le.text()
        self.engine.save_file(name,type)
        self.close()