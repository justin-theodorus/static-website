import os
import shutil


def copy_static_to_output(src="stc", dest="public"):
    # Step 1: Clear the destination if it exists
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"Deleted existing directory: {dest}")

    # Step 2: Create destination directory
    os.makedirs(dest, exist_ok=True)
    print(f"Created directory: {dest}")

    # Step 3: Recursively copy contents
    def recursive_copy(source_path, dest_path):
        if not os.path.exists(dest_path):
            os.makedirs(dest_path, exist_ok=True)

        for item in os.listdir(source_path):
            src_item = os.path.join(source_path, item)
            dest_item = os.path.join(dest_path, item)

            if os.path.isfile(src_item):
                shutil.copy(src_item, dest_item)
                print(f"Copied file: {src_item} → {dest_item}")
            elif os.path.isdir(src_item):
                os.makedirs(dest_item, exist_ok=True)
                print(f"Created subdirectory: {dest_item}")
                recursive_copy(src_item, dest_item)

    recursive_copy(src, dest)


if __name__ == "__main__":
    copy_static_to_output()
