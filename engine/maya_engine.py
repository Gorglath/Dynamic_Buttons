import maya.cmds as cmds
import os
from tool import datas

file_Ending = ["ma", "mb"]

file_types = ["ma", "mb"]

hard_coded_path = 'C:/Users/User/Desktop/SchoolFiles/Pipeline/MOVIE/ASSETS/CAR'


class Maya_Engine(object):

    implements = ['Open', 'Save', 'Reference']

    def open_file(self, Path):
        cmds.file(Path, o=True)

    def save_file(self, Name, type):
        cmds.file(rename=Name)
        if "ma" in type:
            file_format = "mayaAscii"
        else:
            file_format = "mayaBinary"

        cmds.file(save=True, type=file_format)

    def activate_function(self, Name, Path):
        if "Reference" in Name:
            self.reference_file(Path)

    def reference_file(self,Path):
        cmds.file(Path, reference=True)

    def get_files(self):
        return datas.get_files(hard_coded_path, file_Ending)

    def get_file_types(self):
        return file_types

    def get_file_name(self):
        return os.path.basename(cmds.file(query=True, l=True)[0]);
