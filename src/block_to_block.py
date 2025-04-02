import re
from src.blocktype import BlockType

def block_to_block_type(block):
    lines = block.split("\n")

    # CODE BLOCK: starts and ends with ``` on their own line
    if lines[0].strip() == "```" and lines[-1].strip() == "```":
        return BlockType.CODE

    # HEADING: starts with 1–6 '#' followed by space
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    # QUOTE BLOCK: every line starts with '>'
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    # UNORDERED LIST: every line starts with '- '
    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # ORDERED LIST: lines start with 1. 2. 3. ...
    match = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i+1}. "
        if not line.strip().startswith(expected_prefix):
            match = False
            break
    if match:
        return BlockType.ORDERED_LIST

    # If none match, it's a paragraph
    return BlockType.PARAGRAPH