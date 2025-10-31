from picamera2 import Picamera2, Preview
from datetime import datetime
import time
import os

# Paths:
image_save_path = "/home/user2/Chamber2_Folder/Google_Drive/Temp_C2_Holder" # Change this to desired directory - GOOGLE DRIVE!

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
    save_path = image_save_path
    os.makedirs(save_path, exist_ok=True) # Ensure directory exists
    filename = os.path.join(save_path, f"Chamber2_image_{get_current_time()}.jpg")
    return filename

def get_current_time():
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M")
    return timestamp

if __name__ == "__main__":
    main()