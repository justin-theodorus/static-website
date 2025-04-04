import os
import sys
from generate_page import generate_page
from file_utils import copy_static_to_output  

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    output_dir = "docs"  # Always use 'docs' for deployment

    # Step 1: Copy static assets
    copy_static_to_output(dest=output_dir)

    # Step 2: Generate HTML for each markdown file
    print("Looking for markdown files in:", os.path.abspath("content"))
    print("Exists?", os.path.exists("content"))

    for root, dirs, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                print("Generating HTML for:", file)  

                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, "content")
                dest_path = os.path.join(output_dir, relative_path)
                dest_path = dest_path.replace(".md", ".html")

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                generate_page(from_path, "template.html", dest_path, base_path)

if __name__ == "__main__":
    main()
