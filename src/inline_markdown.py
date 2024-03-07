import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != 'text':
            new_list.append(node)
        else:
            text_list = node.text.split(delimiter)
            if len(text_list) == 3:

                new_list.append(TextNode(text_list[0], 'text'))
                new_list.append(TextNode(text_list[1], text_type))
                new_list.append(TextNode(text_list[2], 'text'))
            else:
                new_list.append(node)

    return new_list


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        extract_tuple = extract_markdown_images(node.text)
        if not extract_tuple or node.text_type != 'text':
            new_list.append(node)
        else:
            new_text = node.text
            for tup in extract_tuple:
                text_list = new_text.split(f'![{tup[0]}]({tup[1]})', 1)
                new_list.append(TextNode(text_list[0], 'text'))
                new_list.append(TextNode(tup[0], 'image', tup[1]))
                new_text = text_list[1]
            if new_text != '':
                new_list.append(TextNode(new_text, 'text'))

    return new_list


def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        extract_tuple = extract_markdown_links(node.text)
        if not extract_tuple or node.text_type != 'text':
            new_list.append(node)
        else:
            new_text = node.text
            for tup in extract_tuple:
                text_list = new_text.split(f'[{tup[0]}]({tup[1]})', 1)
                new_list.append(TextNode(text_list[0], 'text'))
                new_list.append(TextNode(tup[0], 'link', tup[1]))
                new_text = text_list[1]
            if new_text != '':
                new_list.append(TextNode(new_text, 'text'))

    return new_list


def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, 'text')], '**', 'bold')
    nodes = split_nodes_delimiter(nodes, '*', 'italic')
    nodes = split_nodes_delimiter(nodes, "`", 'code')
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
