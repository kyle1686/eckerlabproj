from picamera2 import Picamera2, Preview
from datetime import datetime
import time
import os

# Paths:
image_save_dir = "/home/user300/Project_Folder/eckerlabproj/Jupyter_Lab/WorkingVersion/Desktop_Version/Pixels_to_mm/Calibration_Image" # Change this to temporary Calibration Image directory

def take_picture():
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
    os.makedirs(image_save_dir, exist_ok=True) # Ensure directory exists
    time = get_current_time()
    filename = os.path.join(image_save_dir, f"Calibration_at_{time}.jpg")
    return filename

def get_current_time():
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    return timestamp

if __name__ == "__main__":
    take_picture()