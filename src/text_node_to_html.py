from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    text_type = text_node.text_type

    if text_type == TextType.TEXT:
        return LeafNode(None,text_node.text)
    if test_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    if test_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    if test_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    if test_type == TextType.LINK:
        return LeafNode('a', text_node.text, { 'href': text_node.url})
    if test_type == TextType.IMAGE:
        return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
    
    raise Exception("unsupported text type")

