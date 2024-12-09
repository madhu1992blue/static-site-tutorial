from textnode import TextNode, TextType
from htmlnode import HTMLNode
print(TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev"))
print(HTMLNode("a", "linked_text",None, {"href": "https://google.com"})) 
