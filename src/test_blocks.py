from blocks import markdown_to_blocks
import unittest
class TestBlocks(unittest.TestCase):
    def test_to_blocks(self):
        
        markdown = \
"""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        heading = "# This is a heading"
        paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        markdown_list = \
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks[0], heading)
        self.assertEqual(blocks[1], paragraph)
        self.assertEqual(blocks[2], markdown_list)


    def test_extra_lines_between_blocks(self):

        markdown = \
"""# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        heading = "# This is a heading"
        paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        markdown_list = \
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks[0], heading)
        self.assertEqual(blocks[1], paragraph)
        self.assertEqual(blocks[2], markdown_list)
