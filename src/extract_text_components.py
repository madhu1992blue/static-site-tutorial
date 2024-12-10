import re
def extract_markdown_images(text):
    return re.findall(r"!\[((?:\w+ *)+)\]\(([^\)]+)", text)
def extract_markdown_text(text):
    re.findall(r"\[((?:\w+ *)+)\]\(([^\)]+)", text)
