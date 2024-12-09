import unittest

from textnode import TextNode, TextType
from text_node_to_html import text_node_to_html_node
class TestTextNodeToHTMLNode(unittest.TestCase):
    def check_convert_raw_text(self):
        node = TextNode('raw text', TextType.TEXT)
        self.assertEqual(convert_text_node_to_html_node(node).to_html(), 'raw text')

    def check_convert_a_link(self):
        node = TextNode('linked text', TextType.LINK, 'https://example.com')
        self.assertEqual(convert_text_node_to_html_node(node).to_html(), '<a href="https://example.com">raw text</a>')

    def check_convert_img_link(self):
        node = TextNode('alt text', TextType.IMAGE, 'https://example.com')
        self.assertEqual(convert_text_node_to_html_node(node).to_html(), '<img src="https://example.com" alt="alt text"></img>')

    def check_convert_raw_text(self):
        node = TextNode('bold text', TextType.BOLD)
        self.assertEqual(convert_text_node_to_html_node(node).to_html(), '<b>bold text</b>')


