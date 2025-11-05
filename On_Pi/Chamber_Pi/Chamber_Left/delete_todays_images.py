import os
import subprocess

# Paths:
gdrive_remote_path = "gdrive:Chamber/Temp_CLeft_Holder"
temp_image_holder_on_pi = "/home/user2/Chamber2_Folder/Google_Drive/Temp_CLeft_Holder"

def recopy_to_gdrive():
    try:
        subprocess.run(
            ["rclone", "copy", temp_image_holder_on_pi, gdrive_remote_path],
            check=True
        )
        print(f"Successfully copied {temp_image_holder_on_pi} → {gdrive_remote_path}")
    except subprocess.CalledProcessError as e:
        print(f"Upload failed: {e}")
    except FileNotFoundError:
        print("rclone not found — make sure it's installed and in PATH.")
    
def delete_temp_images(directory = temp_image_holder_on_pi):
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