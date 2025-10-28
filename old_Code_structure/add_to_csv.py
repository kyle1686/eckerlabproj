import process_image
import process_soil
import pandas as pd
import os

# Paths:
BASE_DIR = os.getcwd()
greenspace_csv_path = os.path.join(BASE_DIR, "Add in successive folders here", "greenspaces.csv")
soil_moisture_csv_path = os.path.join(BASE_DIR, "Add in successive folders here", "soil_moistures.csv")
master_csv_path = os.path.join(BASE_DIR, "Add in successive folders here", "master_data.csv")

def add_to_csv(image_path, soil_data, csv_path):
    for data in [greenspace_csv_path, soil_moisture_csv_path]:
        new_data = pd.read_csv(data)
    # If Master CSV doesn't exist, create it with headers
    if not os.path.exists(master_csv_path):
        new_data.to_csv(master_csv_path, index=False)
    else:
        # Read existing master CSV
        master_data = pd.read_csv(master_csv_path)
        # Append new data
        updated_df = pd.concat([master_data, new_data], ignore_index=True)
        # Save updated master CSV
        updated_df.to_csv(master_csv_path, index=False)


    # CSV Headers: date/time, image_name, greenspace, soil_moisture

    # Different way, merging data into the columns before adding to the master CSV
    def combine_by_time_and_name(greenspace_csv, moisture_csv, )