import glob


def get_files(path, file_Ending):
    files = []
    for f_end in file_Ending:
        files = files + glob.glob(path + "/**/**/*.{}".format(f_end))
    return files
