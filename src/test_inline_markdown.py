import unittest

from textnode import TextNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


class TestInlineMarkdown(unittest.TestCase):
    def test_split(self):
        old_nodes = [
            TextNode("This is a text 'node'", "text"),
        ]

        self.assertEqual(split_nodes_delimiter(old_nodes, "'", 'code'), [TextNode(
            'This is a text ', 'text'), TextNode('node', 'code'), TextNode('', 'text')])

    def test_extract_images(self):
        extract = extract_markdown_images(
            'This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)')
        self.assertEqual(extract, [("image", "https://i.imgur.com/zjjcJKZ.png"),
                         ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def test_extract_links(self):

        extract = extract_markdown_links(
            'This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and [another](https://i.imgur.com/dfsdkjfd.png)')
        self.assertEqual(extract, [("image", "https://i.imgur.com/zjjcJKZ.png"),
                         ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def test_split_image(self):
        old_nodes = [TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", "text")]
        self.assertEqual([TextNode('This is text with an ', 'text'),
                          TextNode('image', 'image',
                                   'https://i.imgur.com/zjjcJKZ.png'),
                          TextNode(' and another ', 'text'),
                          TextNode('second image', 'image', 'https://i.imgur.com/3elNhQu.png')],
                         split_nodes_image(old_nodes))

    def test_split_link(self):
        old_nodes = [TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)", "text")]
        self.assertEqual([TextNode('This is text with an ', 'text'),
                          TextNode('image', 'link',
                                   'https://i.imgur.com/zjjcJKZ.png'),
                          TextNode(' and another ', 'text'),
                          TextNode('second image', 'link', 'https://i.imgur.com/3elNhQu.png')],
                         split_nodes_link(old_nodes))

    def test_text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)'
        old_nodes = [
            TextNode("This is ", 'text'),
            TextNode("text", 'bold'),
            TextNode(" with an ", 'text'),
            TextNode("italic", 'italic'),
            TextNode(" word and a ", 'text'),
            TextNode("code block", 'code'),
            TextNode(" and an ", 'text'),
            TextNode("image", 'image',
                     "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", 'text'),
            TextNode("link", 'link', "https://boot.dev"),
        ]

        self.assertEqual(old_nodes, text_to_textnodes(text))


if __name__ == "__main__":
    unittest.main()

