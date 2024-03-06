
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="h1", value="blah", props={
                        'key1': 'value1', 'key2': 'value2'})
        node2 = HTMLNode(tag="h1", value="blah",)
        self.assertEqual(node.props_to_html(), 'key1="value1" key2="value2"')
        self.assertEqual(node2.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("h1", "blah", '', {'key1': 'value1', 'key2': 'value2'})
        self.assertEqual(
            repr(node), "HTMLNode(h1, blah, , {'key1': 'value1', 'key2': 'value2'})")

    def test_leafnode(self):
        node = LeafNode(tag='h1', value='Heading 1', props={
                        'key1': 'value1', 'key2': 'value2'})
        self.assertEqual(
            node.to_html(), '<h1 key1="value1" key2="value2">Heading 1</h1>')

    def test_parentnode(self):
        node = ParentNode(tag='h1', children=[ParentNode(
            tag='h2', children=[LeafNode("Normal Text"), LeafNode('Second Node', tag='p')])])
        node2 = ParentNode(tag='div', children=[LeafNode(value='Normal Text', tag='p'), LeafNode(
            'Second Text', tag='a', props={'href': 'https://github.com'})])
        self.assertEqual(
            node.to_html(), '<h1><h2>Normal Text<p>Second Node</p></h2></h1>')
        self.assertEqual(
            node2.to_html(), '<div><p>Normal Text</p><a href="https://github.com">Second Text</a></div>')


if __name__ == "__main__":
    unittest.main()
