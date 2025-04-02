from src.htmlnode import HtmlNode
from src.markdown_to_block import markdown_to_blocks
from src.block_to_block import block_to_block_type
from src.blocktype import BlockType
from src.markdown_pipeline import text_to_textnodes
from src.textnode import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.HEADING:
        level = block.count("#", 0, block.find(" "))
        tag = f"h{level}"
        text = block[level+1:].strip()
        return HtmlNode(tag=tag, children=text_to_children(text))

    elif block_type == BlockType.PARAGRAPH:
        return HtmlNode(tag="p", children=text_to_children(block))

    elif block_type == BlockType.CODE:
        code_inner = "\n".join(block.split("\n")[1:-1])  # skip ```
        code_node = HtmlNode("code", value=code_inner)
        return HtmlNode("pre", children=[code_node])

    elif block_type == BlockType.QUOTE:
        lines = [line.lstrip("> ").strip() for line in block.split("\n")]
        text = " ".join(lines)
        return HtmlNode("blockquote", children=text_to_children(text))

    elif block_type == BlockType.UNORDERED_LIST:
        li_nodes = [
            HtmlNode("li", children=text_to_children(line[2:].strip()))
            for line in block.split("\n")
        ]
        return HtmlNode("ul", children=li_nodes)

    elif block_type == BlockType.ORDERED_LIST:
        li_nodes = [
            HtmlNode("li", children=text_to_children(line[line.find('.')+1:].strip()))
            for line in block.split("\n")
        ]
        return HtmlNode("ol", children=li_nodes)

    else:
        raise ValueError(f"Unknown block type: {block_type}")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(b) for b in blocks]
    return HtmlNode("div", children=children)
