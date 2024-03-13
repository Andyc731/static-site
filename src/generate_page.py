import os

from block_markdown import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path)
    template_file = open(template_path)
    from_file_content = from_file.read()
    template_file_content = template_file.read()
    html = markdown_to_html_node(from_file_content).to_html()
    title = extract_title(from_file_content)
    replace_title = template_file_content.replace("{{ Title }}", title)
    new_html = replace_title.replace("{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    new_file = open(dest_path, "w")
    new_file.write(new_html)

    from_file.close()
    template_file.close()
    new_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        path_content = os.path.join(dir_path_content, file)
        path_dest = os.path.join(dest_dir_path, file)

        if os.path.isfile(path_content):
            path_new_file = path_dest.replace(".md", ".html")
            generate_page(path_content, template_path, path_new_file)
        else:
            generate_pages_recursive(path_content, template_path, path_dest)
