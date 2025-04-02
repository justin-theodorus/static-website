import os
from src.markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 (# ) header found in markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown
    with open(from_path, "r") as f:
        markdown = f.read()

    # Read template
    with open(template_path, "r") as f:
        template = f.read()

    # Convert markdown → HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown)

    # Replace placeholders
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write HTML to file
    with open(dest_path, "w") as f:
        f.write(final_html)

