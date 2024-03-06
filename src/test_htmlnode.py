
import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "blah", '', { 'key1': 'value1', 'key2': 'value2'})
        node2 = HTMLNode("h1", "blah", '')
        self.assertEqual( node.props_to_html(), 'key1="value1" key2="value2" ')
        self.assertEqual( node2.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("h1", "blah", '', { 'key1': 'value1', 'key2': 'value2'})
        self.assertEqual(repr(node), "HTMLNode(h1, blah, , {'key1': 'value1', 'key2': 'value2'})" )


if __name__ == "__main__":
    unittest.main()
