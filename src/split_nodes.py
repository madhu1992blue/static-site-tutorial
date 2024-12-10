from textnode import TextNode, TextType
from extract_text_components import extract_markdown_links, extract_markdown_images
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        
        delimiter_positions = []
        d_pos = node.text.find(delimiter)
        while d_pos != -1:
            delimiter_positions.append(d_pos)
            d_pos = node.text.find(delimiter, d_pos+1)
        if len(delimiter_positions) % 2 != 0:
            raise Exception("Invalid markdown syntax")
        
        if len(delimiter_positions) == 0:
            new_nodes.append(node)
            continue

        split_nodes = []
        started_delimiter = False
        current_pos = 0
        for d_pos in delimiter_positions:
            if current_pos > d_pos: # we exceeded limit
                continue
            if started_delimiter:
                split_nodes.append(TextNode(node.text[current_pos:d_pos], text_type))
                started_delimiter = False
            else:
                split_nodes.append(TextNode(node.text[current_pos:d_pos], TextType.TEXT))
                started_delimiter = True
            current_pos = d_pos + len(delimiter)
        if d_pos != len(node.text) -1:
            split_nodes.append(TextNode(node.text[d_pos + len(delimiter):], TextType.TEXT))
        new_nodes.extend(split_nodes)

    return new_nodes
    



def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for value, href in links:
            link_text = f"[{value}]({href})"
            link_pos = node.text.find(link_text)
            if link_pos == -1:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue

            if link_pos != 0:
                new_nodes.append(TextNode(node.text[:link_pos], TextType.TEXT))
            
            new_nodes.append(TextNode(value, TextType.LINK, href))
            if not node.text.endswith(link_text):
                new_nodes.append(TextNode(node.text[link_pos + len(link_text):], TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for alt_text, src in images:
            image_text = f"![{alt_text}]({src})"
            image_pos = node.text.find(image_text)
            if image_pos == -1:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue

            if image_pos != 0:
                new_nodes.append(TextNode(node.text[:image_pos], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, src))
            if not node.text.endswith(image_text):
                new_nodes.append(TextNode(node.text[image_pos + len(image_text):], TextType.TEXT))
    return new_nodes
