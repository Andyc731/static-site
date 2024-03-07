import unittest

from textnode import TextNode
from block_markdown import block_to_block_type, markdown_to_blocks


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items'''

        self.assertEqual(['This is **bolded** paragraph',
                          'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                          '* This is a list\n* with items'], markdown_to_blocks(text))

    def test_block_to_block_type(self):
        block = markdown_to_blocks('''1.This is a block
        2.This is a new line in same block
        3.another new line
        ''')[0]
        self.assertEqual('ordered_list', block_to_block_type(block))

        block = markdown_to_blocks('''This is a block
        This is a new line in same block
        another new line
        ''')[0]
        self.assertEqual('paragraph', block_to_block_type(block))

        block = markdown_to_blocks('''#####This is a block
        This is a new line in same block
        another new line
        ''')[0]
        self.assertEqual('heading', block_to_block_type(block))

        block = markdown_to_blocks('''*This is a block
        -This is a new line in same block
        -another new line
        ''')[0]
        self.assertEqual('paragraph', block_to_block_type(block))

        block = markdown_to_blocks('''*This is a block
        *This is a new line in same block
        *another new line
        ''')[0]
        self.assertEqual('unordered_list', block_to_block_type(block))

        block = markdown_to_blocks('''```This is a block
        *This is a new line in same block
        *another new line
        ```''')[0]
        self.assertEqual('code', block_to_block_type(block))


if __name__ == "__main__":
    unittest.main()
