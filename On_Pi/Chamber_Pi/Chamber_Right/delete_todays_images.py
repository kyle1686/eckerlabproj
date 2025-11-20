import sys
# Change to repository root, so it can find the config folder with the paths inside it
cr_repo_root = '/home/user300/Salk_Project_Folder/eckerlabproj'
# Add config folder with paths to Python's import search path
if cr_repo_root not in sys.path:
    sys.path.insert(0, cr_repo_root)

import config.paths as paths

import os
import subprocess

def recopy_to_gdrive():
    try:
        subprocess.run(
            ["rclone", "copy", paths.cr_image_save_path, paths.cr_gdrive_remote_path],
            check=True
        )
        print(f"Successfully copied {paths.cr_image_save_path} → {paths.cr_gdrive_remote_path}")
    except subprocess.CalledProcessError as e:
        print(f"Upload failed: {e}")
    except FileNotFoundError:
        print("rclone not found — make sure it's installed and in PATH.")
    
def delete_temp_images(directory = paths.cr_image_save_path):
    deleted = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try: 
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                deleted += 1
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
    print(f"\nDeleted {deleted} image(s) from {directory}")

if __name__ == "__main__":
    recopy_to_gdrive()
    delete_temp_images()