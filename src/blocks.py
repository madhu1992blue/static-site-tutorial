def markdown_to_blocks(markdown):
    blocks = []
    intermediate_lines = []
    for line in markdown.split("\n"):
        if line == "":
            blocks.append("\n".join(intermediate_lines))
            intermediate_lines = []
        else:
            intermediate_lines.append(line)
    return blocks

