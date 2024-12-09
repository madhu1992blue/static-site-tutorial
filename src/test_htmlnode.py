import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_html(self):
        node = HTMLNode('a', 'linked_text', None, {'href':'https://google.com'})
        self.assertEqual(node.props_to_html(),' href="https://google.com"')

    def test_no_props_html(self):
        node = HTMLNode('a', 'linked_text', None, {})
        self.assertEqual(node.props_to_html(),'')

    def test_multiple_props_html(self):
        node = HTMLNode('a', 'linked_text', None, {'href':'https://google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(),' href="https://google.com" target="_blank"')
