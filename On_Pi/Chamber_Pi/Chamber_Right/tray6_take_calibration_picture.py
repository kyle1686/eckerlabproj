import sys
# Change to repository root, so it can find the config folder with the paths inside it
cm_repo_root = '/home/user300/Salk_Project_Folder/eckerlabproj'
# Add config folder with paths to Python's import search path
if cm_repo_root not in sys.path:
    sys.path.insert(0, cl_repo_root)

import config.paths as paths

from picamera2 import Picamera2, Preview
from datetime import datetime
import time
import os

def main():
    picam2 = camera_config()
    time.sleep(2)  # Allow the camera to adjust
    filename = get_file_name()
    picam2.capture_file(filename)
    # print(f"Photo saved as {filename}") # Uncomment for testing

def camera_config():
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    return picam2

def get_file_name():
    save_path = paths.cr_t6_calibimage_save_path
    os.makedirs(save_path, exist_ok=True) # Ensure directory exists
    filename = os.path.join(save_path, f"Tray6_calibration_image_{get_current_time()}.jpg")
    return filename

def get_current_time():
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    return timestamp

if __name__ == "__main__":
    main()