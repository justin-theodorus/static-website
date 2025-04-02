from src.textnode import TextNode, TextType
from src.split_nodes import (
    split_nodes_image,
    split_nodes_link,
    split_nodes_delimiter
)


def text_to_textnodes(text):
    if text.strip() == "":
        return []
    # Start with a single full text node
    
    nodes = [TextNode(text, TextType.TEXT)]

    # First: split inline markdown formatting
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Then: split images and links 
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes