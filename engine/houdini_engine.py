from tool import datas
import hou

file_Ending = ["hipnc"]

file_types = ["hip", "hiplc", "hipnc"]

hard_coded_path = 'C:/Users'


class Houdini_Engine(object):

    implements = ['Open', 'Save', 'Merge']

    def open_file(self, path):
        hou.hipFile.load(path)

    def save_file(self, Name, type):
        file_path = Name + "." + type
        hou.hipFile.save(file_path)

    def activate_function(self, Name, Path):
        if 'Merge' in Name:
            self.merge_file(Path)

    def merge_file(self, path):
        hou.hipFile.merge(path)

    def get_files(self):
        return datas.get_files(hard_coded_path, file_types)

    def get_file_types(self):
        return file_types

    def get_file_name(self):
        return hou.hipFile.basename()
