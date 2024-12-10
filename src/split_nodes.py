from textnode import TextNode, TextType

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
        
