import maya.cmds as cmds
import os
from tool import datas

file_Ending = ["ma", "mb"]

file_types = ["ma", "mb"]

hard_coded_path = 'C:/Users/User/Desktop/SchoolFiles/Pipeline/MOVIE/ASSETS/CAR'


class Maya_Engine(object):

    implements = ['Open', 'Save', 'Reference']

    def open_file(self, path):
        cmds.file(path, o=True)

    def save_file(self, name, type):
        cmds.file(rename=name)
        if "ma" in type:
            file_format = "mayaAscii"
        else:
            file_format = "mayaBinary"

        cmds.file(save=True, type=file_format)

    def activate_function(self, name, path):
        if "Reference" in name:
            self.reference_file(path)

    def reference_file(self, path):
        cmds.file(path, reference=True)

    def get_files(self):
        return datas.get_files(hard_coded_path, file_Ending)

    def get_file_types(self):
        return file_types

    def get_file_name(self):
        return os.path.basename(cmds.file(query=True, l=True)[0]);
