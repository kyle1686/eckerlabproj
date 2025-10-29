#!/usr/bin/env python
# coding: utf-8

# In[131]:


# only needed in Jupyter Lab to see the images inline
# get_ipython().run_line_magic('matplotlib', 'widget')

from plantcv import plantcv as pcv
from plantcv.parallel import WorkflowInputs
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import json
import shutil


def process_single_chamber2_image(filename, BASE_DIR, image_dir):
    # Central Path Locations
    # print(f"Base Directory = {BASE_DIR}")

    image_name = filename
    image_path = os.path.join(image_dir, image_name)
    
    # Change to Chamber folder: this is where the temporary data on pixel number in plants is saved
    temp_chamber_image_results = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/On_Laptop/Chamber_Jupyter_Labs/Chamber2/temp_chamber_image_results.json" #CHANGE TO LOCAL GITHUB REPO
    # Change to location where data from this run is saved
    analysis_results_csv_path = "/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Final_Data/chamber_analysis_log.csv"
    # Change to location where scale_values is saved
    scale_values_path = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/On_Laptop/Chamber_Jupyter_Labs/Chamber2/Pixels_to_mm_C2/scale_values.json" #CHANGE TO LOCAL GITHUB REPO
    # Change to location where plant_names.csv is saved
    plant_names_path = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/On_Laptop/Chamber_Jupyter_Labs/plant_names.csv"

    
    # Splitting filename to get the time
    name_without_ext, _ = os.path.splitext(filename)
    name_parts = name_without_ext.split('_')
    time = name_parts[2]

    
    # Input/output options for PlantCV
    args = WorkflowInputs(
        images=[image_path],
        names="image1",
        result=temp_chamber_image_results, 
        outdir=".",
        writeimg=False,
        debug=None
        )
    
    
    # Set debug to the global parameter 
    pcv.params.debug = args.debug
    # Change display settings
    pcv.params.dpi = 100
    # Increase text size and thickness to make labels clearer
    # (size may need to be altered based on original image size)
    pcv.params.text_size = 10
    pcv.params.text_thickness = 20
    
    
    # Shows your image, defines it as "img"
    img, path, filename = pcv.readimage(filename=args.image1)
    
    
    # Crops your image
    crop_img = pcv.crop(img=img, x=1072, y=303, w=2872-1072, h=2050-303)
    
    
    # Shows options for which channel to view the image through (ideally want the most contrast)
    colorspace_img = pcv.visualize.colorspaces(rgb_img=crop_img)
    
    
    # Actually picks a channel with rgb2gray_"lab" and then the channel is the letter from "lab" that you look through
    channeled_img = pcv.rgb2gray_lab(rgb_img=crop_img, channel='a')
    
    
    # Masks the image
    thresh_mask = pcv.threshold.binary(gray_img=channeled_img, threshold=128, object_type='dark')
    
    
    # Deletes groups of pixels less than the pixel size (weird dots around edges not plant is unmasked)
    cleaned_mask = pcv.fill(bin_img=thresh_mask, size=160)
    
    
    # Defines many Region of Interests (ROI) which selects white pixels and deselects black pixels from a masked image, based from little circles around each plant with coordinates we define
    rois = pcv.roi.multi(img=cleaned_mask, 
                        coord=[(156,176), (364,166), (563,176), (752,171), 
                               (1031,157), (1220,161), (1433,157), (1622,128), 
                               (142,488), (336,445), (525,417), (743,417), 
                               (998,436), (1225,454), (1428,445), (1622,426), 
                               (147,752), (360,719), (544,695), (762,738), 
                               (1026,729), (1206,719), (1428,681), (1650,743), 
                               (161,1022), (374,998), (563,989), (799,989), 
                               (1031,1012), (1234,979), (1466,974), (1660,989), 
                               (166,1310), (379,1286), (566,1258), (776,1253), 
                               (1050,1277), (1248,1267), (1447,1277), (1678,1282), 
                               (123,1551), (1031,1584)],
                        radius=30)
    
    
    # Label and number objects in ROI; A good check to ensure different plants are different objects from being different colors
    labeled_mask, num_plants = pcv.create_labels(mask=cleaned_mask, rois=rois, roi_type='partial')
    
    # Outputs analyzed image
    shape_image = pcv.analyze.size(img=crop_img, labeled_mask=labeled_mask, n_labels=num_plants)
    
    
    # Saves results for the 1 image (running again overwites past results)
    pcv.outputs.save_results(filename= args.result, outformat="json")
    
    
    # Gets pixels to mm scalar s (mm per pixel, so: pixels * s^2 = mm^2)
    with open(scale_values_path, "r") as f:
        scale_data = json.load(f)
    
    mean_s = scale_data["mean_scale_mm_per_pixel"]
    std_s = scale_data["std_scale_mm_per_pixel"]
    
    
    # Create single-row DataFrame and write it to an analysis results csv
    df = pd.read_csv(plant_names_path)
    for i in list(range(43,85)): # starts at first number, goes up to but not including second number
        pixels_value = pcv.outputs.observations[f"default_{i-42}"]["area"]["value"]
        plant_number = f"plant{i}"
        plant_ID = df.loc[df["old_plant_number"] == plant_number, "new_name"].values[0]
        stress = df.loc[df["old_plant_number"] == plant_number, "stress"].values[0]
        new_data = pd.DataFrame([{
            "time": time,
            "plant_number": plant_number,
            "plant_ID": plant_ID,
            "Area (mm^2)": pixels_value * (mean_s ** 2),
            "Stress (%)": stress
            # "Uncertainty (mm^2)": pixels_value * 2 * mean_s * std_s
        }])
        # If analysis_log.csv doesn't exist, creates it with a header:
        if not os.path.isfile(analysis_results_csv_path):
            new_data.to_csv(analysis_results_csv_path, index=False)
        else:
            # Append without writing header again
            new_data.to_csv(analysis_results_csv_path, mode='a', header=False, index=False)
    
    
    # Moves image to longterm storage
    short_term_dir = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Temp_C2_Holder'
    long_term_dir = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Longterm_Image_Storage'
    filename = image_name
    
    # Full paths
    src_path = os.path.join(short_term_dir, filename)
    dst_path = os.path.join(long_term_dir, filename)
    
    # Ensure long-term folder exists
    os.makedirs(long_term_dir, exist_ok=True)
    
    # Moves file to long-term folder
    shutil.move(src_path, dst_path)


def process_all_chamber2_images():
    BASE_DIR = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber'
    image_dir = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Temp_C2_Holder'
    files = [f for f in os.listdir(image_dir) if not f.startswith(".")]
    if len(files) == 0:
        raise FileNotFoundError(f"No image files found in {image_dir}.")
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(image_dir, x)))
    print(f"Found {len(files)} images to process.\n")
    for i,filename in enumerate(files, start=1):
        print(f"({i}/{len(files)}) Processing image: {filename}")
        try:
            process_single_chamber2_image(filename, BASE_DIR, image_dir)
            print(f"Finished processing {filename}.\n")
        except Exception as e:
            print(f"Error processing {filename}: {e}\n")
    print("Chamber 2 image processing completed.\n")

if __name__ == "__main__":
    process_all_chamber2_images()