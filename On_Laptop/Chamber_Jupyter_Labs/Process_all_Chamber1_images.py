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


def process_single_chamber1_image(filename, BASE_DIR, image_dir):
    # Central Path Locations
    # print(f"Base Directory = {BASE_DIR}")

    image_name = filename
    image_path = os.path.join(image_dir, image_name)
    
    # Change to Chamber folder: this is where the temporary data on pixel number in plants is saved
    temp_chamber_image_results = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/On_Laptop/Chamber_Jupyter_Labs/Chamber1/temp_chamber_image_results.json" #CHANGE TO LOCAL GITHUB REPO
    # Change to location where data from this run is saved
    analysis_results_csv_path = "/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Final_Data/chamber_analysis_log.csv"
    # Change to location where scale_values is saved
    scale_values_path = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/On_Laptop/Chamber_Jupyter_Labs/Chamber1/Pixels_to_mm_C1/scale_values.json" #CHANGE TO LOCAL GITHUB REPO
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
    crop_img = pcv.crop(img=img, x=980, y=305, w=1773, h=1769)

    
    # Actually picks a channel with rgb2gray_"lab" and then the channel is the letter from "lab" that you look through
    channeled_img = pcv.rgb2gray_cmyk(rgb_img=crop_img, channel='m')


    # Masks the image
    thresh_mask = pcv.threshold.binary(gray_img=channeled_img, threshold=175, object_type='dark')
    
    
    # Deletes groups of pixels less than the pixel size (weird dots around edges not plant is unmasked)
    cleaned_mask = pcv.fill(bin_img=thresh_mask, size=250)
    
    
    # Defines many Region of Interests (ROI) which selects white pixels and deselects black pixels from a masked image, based from little circles around each plant with coordinates we define
    rois = pcv.roi.multi(img=cleaned_mask, 
                        coord=[(82,168), (307,153), (503,163), (738,158), 
                               (1049,186), (1264,196), (1460,196), (1657,172), 
                               (106,483), (292,426), (517,459), (728,469), 
                               (1030,488), (1211,507), (1438,526), (1642,507), 
                               (91,766), (302,747), (508,751), (723,785), 
                               (996,804), (1192,761), (1441,751), (1654,814), 
                               (77,1034), (312,1039), (508,1039), (723,1034), 
                               (986,1072), (1202,1077), (1446,1086), (1659,1110), 
                               (101,1331), (321,1345), (522,1321), (723,1297), 
                               (972,1331), (1192,1369), (1393,1393), (1599,1393), 
                               (96,1601), (972,1607)],
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
    for i in list(range(1,43)): # starts at first number, goes up to but not including second number
        pixels_value = pcv.outputs.observations[f"default_{i}"]["area"]["value"]
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
    short_term_dir = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Temp_C1_Holder'
    long_term_dir = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Longterm_Image_Storage'
    filename = image_name
    
    # Full paths
    src_path = os.path.join(short_term_dir, filename)
    dst_path = os.path.join(long_term_dir, filename)
    
    # Ensure long-term folder exists
    os.makedirs(long_term_dir, exist_ok=True)
    
    # Moves file to long-term folder
    shutil.move(src_path, dst_path)


def process_all_chamber1_images():
    BASE_DIR = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber'
    image_dir = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Temp_C1_Holder'
    files = [f for f in os.listdir(image_dir) if not f.startswith(".")]
    if len(files) == 0:
        raise FileNotFoundError(f"No image files found in {image_dir}.")
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(image_dir, x)))
    print(f"Found {len(files)} images to process.\n")
    for i,filename in enumerate(files, start=1):
        print(f"({i}/{len(files)}) Processing image: {filename}")
        try:
            process_single_chamber1_image(filename, BASE_DIR, image_dir)
            print(f"Finished processing {filename}.\n")
        except Exception as e:
            print(f"Error processing {filename}: {e}\n")
    print("Chamber 1 image processing completed.\n")

if __name__ == "__main__":
    process_all_chamber1_images()