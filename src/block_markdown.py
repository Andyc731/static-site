import re

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from inline_markdown import text_to_textnodes
from textnode import TextNode


def markdown_to_blocks(markdown):
    new_lines = markdown.split("\n\n")
    empty_index = []
    for i in range(len(new_lines)):
        if new_lines[i] == "\n" or new_lines[i] == "":
            empty_index.append(i)
        else:
            new_lines[i] = new_lines[i].strip()
    for index in empty_index:
        new_lines.pop(index)

    return new_lines


def block_to_block_type(block):
    if block.startswith("#"):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        block_type = "quote"
        for line in block.split("\n"):
            if not line.strip().startswith(">"):
                block_type = "paragraph"
        return block_type_quote
    if block.startswith("*") or block.startswith("-"):
        block_type = "unordered_list"
        for line in block.split("\n"):
            if not line.strip().startswith("*") and not line.startswith("-"):
                block_type = "paragraph"
        return block_type_ulist
    if block.startswith("1."):
        block_type = "ordered_list"
        line = block.split("\n")
        for i in range(1, len(line) + 1):
            if not line[i - 1].strip().startswith(f"{i}."):
                block_type = "paragraph"
        return block_type_olist
    return block_type_paragraph


def block_type_heading(block):
    count = 0
    new_block = block
    while new_block[0] == "#":
        count += 1
        new_block = new_block[1:]
    new_block = block.lstrip("# ")
    html_nodes = block_to_html_node(new_block)
    return ParentNode(html_nodes, f"h{count}")


def block_type_code(block):
    new_block = block.strip("```")
    stripped_block = new_block.strip("\n ")
    html_nodes = block_to_html_node(stripped_block)
    return ParentNode([ParentNode(html_nodes, "code")], "pre")


def block_type_ulist(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        inline_html_nodes = []
        text_nodes = text_to_textnodes(line.lstrip("*- "))
        for text_node in text_nodes:
            inline_html_nodes.append(text_node_to_html_node(text_node))
        li_nodes.append(ParentNode(inline_html_nodes, "li"))

    return ParentNode(li_nodes, "ul")


def block_type_olist(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        inline_html_nodes = []
        new_line = re.sub(r"^\d+\.\s*", "", line)
        text_nodes = text_to_textnodes(new_line)
        for text_node in text_nodes:
            inline_html_nodes.append(text_node_to_html_node(text_node))
        li_nodes.append(ParentNode(inline_html_nodes, "li"))
    return ParentNode(li_nodes, "ol")


def block_type_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip("> "))
    new_block = "\n".join(new_lines)
    html_nodes = block_to_html_node(new_block)

    return ParentNode(html_nodes, "blockquote")


def block_type_paragraph(block):
    html_nodes = block_to_html_node(block)
    return ParentNode(html_nodes, "p")


def block_to_html_node(block):
    html_nodes = []
    new_block = block.replace("\n", "\n ")
    lines = new_block.split("\n")
    for line in lines:
        text_nodes = text_to_textnodes(line)
        for text_node in text_nodes:
            html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        nodes.append(block_type(block))

    return ParentNode(nodes, "div")
