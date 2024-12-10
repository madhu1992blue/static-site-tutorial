from enum import Enum
def markdown_to_blocks(markdown):
    blocks = []
    intermediate_lines = []
    for line in markdown.split("\n"):
        if line == "":
            if len(intermediate_lines) == 0:
                continue
            blocks.append("\n".join(intermediate_lines).strip())
            intermediate_lines = []
        else:
            intermediate_lines.append(line)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("# "):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    is_quote = True
    for line in block.split("\n"):
        if not line.startswith("> "):
            is_quote = False
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list, is_ordered_list = True, True
    line_counter = 1
    for line in block.split("\n"):
        if (not line.startswith("- ")) and (not line.startswith("* ")):
            is_unordered_list = False
        if not line.startswith(f"{line_counter}. "):
            is_ordered_list = False
        line_counter += 1

    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    


