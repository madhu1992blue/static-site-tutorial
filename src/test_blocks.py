from blocks import markdown_to_blocks, block_to_block_type, BlockType
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

    def test_block_to_block_type(self):
        unordered_list = block_to_block_type(
"""* a
* b""")

        ordered_list = block_to_block_type("""1. a
2. b""")
        quote = block_to_block_type("""> a
> v""")
        code = block_to_block_type("""```
<html></html>```""")
        
        paragraph = block_to_block_type("""* a
1. b""")
        heading = block_to_block_type("""# This is a heading""")
        heading3 = block_to_block_type("""## This is a l3 heading""")
        self.assertEqual(heading3, BlockType.HEADING)
        self.assertEqual(heading, BlockType.HEADING)
        self.assertEqual(unordered_list, BlockType.UNORDERED_LIST)
        self.assertEqual(ordered_list,BlockType.ORDERED_LIST)
        self.assertEqual(quote, BlockType.QUOTE)
        self.assertEqual(code, BlockType.CODE)
        self.assertEqual(paragraph, BlockType.PARAGRAPH)
