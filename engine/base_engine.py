import sys


def get_engine():
    if 'maya' in sys.executable:
        from engine import maya_engine as me
        return me.Maya_Engine()
    elif 'houdini' in sys.executable:
        from engine import houdini_engine as he
        return he.Houdini_Engine()