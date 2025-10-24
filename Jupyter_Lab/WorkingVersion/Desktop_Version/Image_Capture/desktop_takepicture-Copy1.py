from picamera2 import Picamera2, Preview
from datetime import datetime
import time
import os

# Paths:
image_save_dir = "eckerlabproj/Jupyter_Lab/WorkingVersion/Desktop_Version/Image_Holder/Temp_Staging_Area" # Change this to temporary staging directory
possible_types_path = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/Jupyter_Lab/WorkingVersion/Desktop_Version/Image_Capture/possible_types.csv" # Change this to where the possible genotypes and stress list for the plates we're working with is

# Temporary
genotypes=["Salk_080561c", "Col-0", "Salk_098896", "SailSeq_201_G03", "Salk_052070", "Salk_50.E01.1", "Salk_203144", "SailSeq_5_E01.1", "Salk_102761c", "Salk_056202c", "Salk_002822c"]
stress = [100, 25]

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
    os.makedirs(image_save_dir, exist_ok=True) # Ensure directory exists
    while True:
        genotype = get_genotype()
        stress = get_stress()
        print(f"\nSelected → Genotype: {genotype}, Stress: {stress}")
        confirmation_input = print(f"\nSatisfied? (Enter to confirm, \"r\" to redo): ")
        if confirmation_input.lower().strip() != r:
            break
    filename = os.path.join(image_save_dir, f"{genotype}_{stress}_{get_current_time()}.jpg")
    return filename

def get_genotype():
    genotype_input = int(input("Enter genotype number: "))
    return genotypes[genotype_input]

def get_stress():
    stress_input = int(input("Enter stress number: "))
    return stress[stress_input]

def get_current_time():
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    return timestamp

if __name__ == "__main__":
    main()