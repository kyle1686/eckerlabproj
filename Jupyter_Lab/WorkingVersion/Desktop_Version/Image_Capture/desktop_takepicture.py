from picamera2 import Picamera2, Preview
from datetime import datetime
import pandas as pd
import time
import os

# Paths:
image_save_dir = "eckerlabproj/Jupyter_Lab/WorkingVersion/Desktop_Version/Image_Holder/Temp_Staging_Area" # Change this to temporary staging directory
possible_types_path = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/Jupyter_Lab/WorkingVersion/Desktop_Version/Image_Capture/possible_types.csv" # Change this to where the possible genotypes and stress list for the plates we're working with is

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
    os.makedirs(save_path, exist_ok=True) # Ensure directory exists
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
    df = pd.read_csv(possible_types_path)
    unique_genotype_options = df[['genotype_number', 'genotype']].drop_duplicates()
    print("Possible Genotype Selections (edit possible_types.csv if incorrect):")
    for _, row in unique_genotype_options.iterrows():
        print(f"{row['genotype_number']}: {row['genotype']}")
    genotype_input = int(input("Enter genotype number: "))
    genotype = df[df['genotype_number'] == g_num]['genotype'].iloc[0]
    return genotype

def get_stress():
    df = pd.read_csv(possible_types_path)
    unique_stress_options = df[['stress_number', 'stress']].drop_duplicates()
    print("Possible Stress Selections (edit possible_types.csv if incorrect):")
    for _, row in unique_stress_options.iterrows():
        print(f"{row['stress_number']}: {row['stress']}")
    stress_input = int(input("Enter stress number: "))
    stress = df[df['stress_number'] == s_num]['stress'].iloc[0]
    return stress

def get_current_time():
    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    return timestamp

if __name__ == "__main__":
    main()