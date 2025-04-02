import os
import shutil


def copy_static_to_public(src="stc", dest="public"):
    # Step 1: Clear the destination if it exists
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"Deleted existing directory: {dest}")

    # Step 2: Create a fresh public directory
    os.mkdir(dest)
    print(f"Created directory: {dest}")

    # Step 3: Walk through and copy contents
    def recursive_copy(source_path, dest_path):
        for item in os.listdir(source_path):
            src_item = os.path.join(source_path, item)
            dest_item = os.path.join(dest_path, item)

            if os.path.isfile(src_item):
                shutil.copy(src_item, dest_item)
                print(f"Copied file: {src_item} → {dest_item}")
            elif os.path.isdir(src_item):
                os.mkdir(dest_item)
                print(f"Created subdirectory: {dest_item}")
                recursive_copy(src_item, dest_item)

    recursive_copy(src, dest)



if __name__ == "__main__":
    copy_static_to_public()
    
