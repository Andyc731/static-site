import re


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url

    def repr(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_list.append(node)
        else:
            if node.text_type == 'text':
                text_list = node.text.split(delimiter)
                if len(text_list) == 3:

                    new_list.append(TextNode(text_list[0], 'text'))
                    new_list.append(TextNode(text_list[1], text_type))
                    new_list.append(TextNode(text_list[2], 'text'))
    return new_list


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        extract_tuple = extract_markdown_images(node.text)
        if not extract_tuple:
            new_list.append(node)
        else:
            new_text = node.text
            for tup in extract_tuple:
                text_list = new_text.split(f'![{tup[0]}]({tup[1]})', 1)
                new_list.append(TextNode(text_list[0], 'text'))
                new_list.append(TextNode(tup[0], 'image', tup[1]))
                new_text = text_list[1]
    return new_list


def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        extract_tuple = extract_markdown_links(node.text)
        if not extract_tuple:
            new_list.append(node)
        else:
            new_text = node.text
            for tup in extract_tuple:
                text_list = new_text.split(f'[{tup[0]}]({tup[1]})', 1)
                new_list.append(TextNode(text_list[0], 'text'))
                new_list.append(TextNode(tup[0], 'image', tup[1]))
                new_text = text_list[1]
    return new_list
