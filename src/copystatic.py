import os
import shutil


def copystatic(path_static, path_public):
    if not os.path.exists(path_public):
        os.mkdir(path_public)

    for file in os.listdir(path_static):
        path_from = os.path.join(path_static, file)
        path_to = os.path.join(path_public, file)

        print(f"copying {path_from} to {path_to}")

        if os.path.isfile(path_from):
            shutil.copy(path_from, path_to)
        else:
            copystatic(path_from, path_to)
