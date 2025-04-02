from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links  

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split text nodes of type TEXT
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        
        # If delimiter doesn't exist, keep node as is
        if len(parts) == 1:
            new_nodes.append(node)
            continue

        # Alternate between TEXT and the given text_type
        for i, part in enumerate(parts):
            if part == "":
                continue 
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue

        # Rebuild text by inserting text and image nodes
        remaining = text
        for alt, url in images:
            img_md = f"![{alt}]({url})"
            idx = remaining.find(img_md)
            if idx > 0:
                new_nodes.append(TextNode(remaining[:idx], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url=url, alt=alt))
            remaining = remaining[idx + len(img_md):]

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes
def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue

        # Rebuild text by inserting text and image nodes
        remaining = text
        for alt, url in links:
            link_md = f"[{alt}]({url})"
            idx = remaining.find(link_md)
            if idx > 0:
                new_nodes.append(TextNode(remaining[:idx], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url=url))
            remaining = remaining[idx + len(link_md):]

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes