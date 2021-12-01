import glob


def get_files(Path,file_Ending):
    files = []
    for f_end in file_Ending:
        files = files + glob.glob(Path + "/**/**/*.{}".format(f_end))
    return files
