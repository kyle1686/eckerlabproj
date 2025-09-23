# useful things to do on the raspberry pi: 
#  - sudo apt install -y python3-opencv
#  - sudo apt install -y opencv-data

# this is useful 
# https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

from picamera2 import Picamera2, Preview
from constants import *
import numpy as np
import time

# format of the filename is yyyy-mm-dd--HH-MM-SS, e.g., 2022-08-01--11:59:59.csv
def gen_data_filename():
    return DATA_FILE_RELATIVE_DIR + dt.today().strftime(TIME_FORMAT)

# (taken and modified from picamera2 documentation)
# The following script will:
#   1. Open the camera system
#   2. Generate a camera configuration suitable for preview
#   3. Configure the camera system with that preview configuration
#   4. Start the preview window
#   5. Start the camera running
#   6. Wait for N hour(s) and capture a JPEG file (still in the preview resolution)
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL) # GUI implementation? non-GUI is Preview.DRM
picam2.start(show_preview=True)
time.sleep(3600 * N) # 3600 seconds in an hour; N is the number of hours

# a blue overlay, though i think its just a display and doesnt save with the image 
overlay = np.zeros((OVERLAY_HEIGHT, OVERLAY_WIDTH, 4), dtype=np.uint8)
overlay[:, :] = = (0, 0, 255, 128) # blueish, the last number is opacity
picam2.set_overlay(overlay) 

# possible values: 'jpeg', 'png', 'bmp' or 'gif'
# idk what opencv uses but probably one of these
picam2.capture_file(gen_data_filename() + ".jpg") 



