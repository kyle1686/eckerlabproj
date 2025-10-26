from desktop_takepicture import take_picture
from Process_Desktop import process_desktop_images

# Make sure to have run the scale value calibration first before using this script

def run_all():
    # Step 1: Capture Image
    take_picture()
    
    # Step 2: Process Captured Images
    process_desktop_images()

if __name__ == "__main__":
    run_all()