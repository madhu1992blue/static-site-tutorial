import unittest
from parentnode import ParentNode
from leafnode import LeafNode
class TestParentNode(unittest.TestCase):
    def test_parent_render(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_child_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", {'id': 'bold'} ),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b id="bold">Bold text</b>Normal text</p>')

    def test_deep_render(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("b", [LeafNode("i", "deeper node")])
            ],
            {"id": "para-id"}
        )
        self.assertEqual(node.to_html(), '<p id="para-id"><b>Bold text</b>Normal text<i>italic text</i>Normal text<b><i>deeper node</i></b></p>')
