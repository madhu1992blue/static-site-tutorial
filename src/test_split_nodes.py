from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
import unittest
from textnode import TextNode, TextType


class TestSplitNodesLinks(unittest.TestCase):
    def test_split_link(self):
        nodes = [TextNode("This is a [link to google](https://google.com)", TextType.TEXT)]
        expected_nodes = [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link to google", TextType.LINK, "https://google.com"),
        ]
        
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(expected_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)

    def test_split_image(self):
        nodes = [TextNode("This is a ![link to google](https://google.com)", TextType.TEXT)]
        expected_nodes = [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link to google", TextType.IMAGE, "https://google.com"),
        ]

        new_nodes = split_nodes_image(nodes)
        print(new_nodes)
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(expected_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)

    def test_split_no_link(self):
        nodes = [TextNode("This is a ![link to google](https://google.com)", TextType.TEXT)]
        expected_nodes = [
                TextNode("This is a ![link to google](https://google.com)", TextType.TEXT),
        ]

        new_nodes = split_nodes_link(nodes)
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(expected_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)

    def test_split_no_image(self):
        nodes = [TextNode("This is a [link to google](https://google.com)", TextType.TEXT)]
        expected_nodes = [
                TextNode("This is a [link to google](https://google.com)", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(expected_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        print(new_nodes)
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)

    def test_multi_char_delimiter(self):
        node = TextNode("This is text with a **italic text** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)

    def test_text_with_no_delimiter(self):
        node = TextNode("This is text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text", TextType.TEXT),
        ]
        self.assertEqual(len(new_nodes), len(expected_nodes))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].text, expected_nodes[i].text)
            self.assertEqual(new_nodes[i].text_type, expected_nodes[i].text_type)
