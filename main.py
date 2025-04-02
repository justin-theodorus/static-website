import os
from generate_page import generate_page
from src.main import copy_static_to_public  

def main():
    # Step 1: Clean and copy static files
    copy_static_to_public()

    # Step 2: Walk through the content folder recursively
    for root, dirs, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)

                # Turn content/blog/glorfindel/index.md into public/blog/glorfindel/index.html
                relative_path = os.path.relpath(from_path, "content")
                dest_path = os.path.join("public", relative_path)
                dest_path = dest_path.replace(".md", ".html")

                # Ensure directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Generate the page
                generate_page(from_path, "template.html", dest_path)

if __name__ == "__main__":
    main()
