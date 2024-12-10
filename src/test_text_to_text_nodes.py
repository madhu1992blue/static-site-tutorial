import unittest

from text_to_text_nodes import text_to_text_nodes
from textnode import TextNode, TextType
class TestTextToTextNodes(unittest.TestCase):
    def test_conversion(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result_nodes = text_to_text_nodes(text)

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        print(result_nodes)
        self.assertEqual(len(expected_nodes), len(result_nodes))
        for i in range(len(expected_nodes)):
            self.assertEqual(result_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(result_nodes[i].text_type, expected_nodes[i].text_type)
