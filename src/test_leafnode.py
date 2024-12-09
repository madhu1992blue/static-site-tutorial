import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_raw_text(self):
        node = LeafNode(None, 'This is a raw text', None)
        self.assertEqual(node.to_html(), 'This is a raw text')

    def test_tag_leaf(self):
        node = LeafNode('p', 'This is a paragraph', None)
        self.assertEqual(node.to_html(), '<p>This is a paragraph</p>')

    def test_tag_with_attributes(self):
        node = LeafNode('p', 'This is a paragraph', { 'id': 'para-id'})
        self.assertEqual(node.to_html(), '<p id="para-id">This is a paragraph</p>')
