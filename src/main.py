import os
import shutil

from copystatic import copystatic

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copystatic(dir_path_static, dir_path_public)


main()
