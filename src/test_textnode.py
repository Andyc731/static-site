import unittest

from textnode import TextNode, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

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
                          TextNode('image', 'image',
                                   'https://i.imgur.com/zjjcJKZ.png'),
                          TextNode(' and another ', 'text'),
                          TextNode('second image', 'image', 'https://i.imgur.com/3elNhQu.png')],
                         split_nodes_link(old_nodes))


if __name__ == "__main__":
    unittest.main()
