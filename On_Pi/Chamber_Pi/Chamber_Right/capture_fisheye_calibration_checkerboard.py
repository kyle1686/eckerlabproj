import sys
# Change to repository root, so it can find the config folder with the paths inside it
cr_repo_root = '/home/user300/Salk_Project_Folder/eckerlabproj'
# Add config folder with paths to Python's import search path
if cr_repo_root not in sys.path:
    sys.path.insert(0, cr_repo_root)

import config.paths as paths
import subprocess
from picamera2 import Picamera2, Preview
from datetime import datetime
import time
import os


def main():
    while True:
        picam2 = camera_config()
        time.sleep(2)  # Allow the camera to adjust
        filename = get_file_name()
        picam2.capture_file(filename)
        print(f"Photo saved as {filename}.\n")
        again = input("Do you want to capture another image (y), copy to Google Drive and rerun (g), or end with copying to Google Drive (anything)?: ")
        if again.lower() == "y":
            continue
        if again.lower() == "g":
             copy_to_drive()
             # print(f"Photo saved as {filename}")
             continue
        else:
            break
    copy_to_drive()
    print("Images captured and uploaded to the Google Drive folder successfully.")

def camera_config():
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    return picam2

def get_file_name():
    save_path = paths.cr_checkerboard_calibration_onpi
    os.makedirs(save_path, exist_ok=True) # Ensure directory exists
    filename = os.path.join(save_path, f"ChamberRight_checkerboard_{get_current_time()}.jpg")
    return filename

def get_current_time():
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    return timestamp

def copy_to_drive():
    try:
        subprocess.run(
            ["rclone", "copy", paths.cr_checkerboard_calibration_onpi, paths.cr_gdrive_checkerboard_images],
            check=True
        )
        print(f"Successfully copied {paths.cr_checkerboard_calibration_onpi} → {paths.cr_gdrive_checkerboard_images}")
    except subprocess.CalledProcessError as e:
        print(f"Upload failed: {e}")
    except FileNotFoundError:
        print("rclone not found — make sure it's installed and in PATH.")

if __name__ == "__main__":
    main()