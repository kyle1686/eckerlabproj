from Process_all_Chamber1_images import process_all_chamber1_images
from Process_all_Chamber2_images import process_all_chamber2_images

# Make sure to have run the scale value calibration first before using this script

def run_all_chamber():
    process_all_chamber1_images()
    process_all_chamber2_images()
    print("All chamber image processing complete.")
    
if __name__ == "__main__":
    run_all_chamber()