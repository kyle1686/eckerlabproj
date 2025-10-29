import os
import subprocess

# Paths:
temp_image_holder_dir = "/home/chamberuser1/Chamber1Folder/Google_Drive/Temp_C1_Holder" # Change this to desired directory - GOOGLE DRIVE!

def recopy_to_gdrive():
    gdrive_remote_path = "gdrive:Chamber/Temp_C1_Holder"
    temp_image_holder_on_pi = "/home/chamberuser1/Chamber1Folder/Google_Drive/Temp_C1_Holder"
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
    
def delete_temp_images(directory = temp_image_holder_dir):
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