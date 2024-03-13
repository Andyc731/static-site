import os
import shutil

from copystatic import copystatic
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"

path_markdown = "./content/"
path_template_html = "./template.html"
path_dest = "./public/"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copystatic(dir_path_static, dir_path_public)

    generate_pages_recursive(path_markdown, path_template_html, path_dest)


main()
