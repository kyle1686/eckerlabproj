#!/usr/bin/env python
# coding: utf-8

# In[1]:


# only needed in Jupyter Lab to see the images inline
# get_ipython().run_line_magic('matplotlib', 'widget')

import os
# os.environ["QT_QPA_PLATFORM"] = "offscreen"
from plantcv import plantcv as pcv
from plantcv.parallel import WorkflowInputs
# import matplotlib.pyplot as plt
import pandas as pd
import json
import shutil


def process_single_desktop_image(filename, BASE_DIR):
    # In[2]:


    # Central Path Locations

    # Makes Base Directory where this script is running from:
    # BASE_DIR = os.getcwd()
    # To access more than just what's in your Base Directory, use the following:
    # BASE_DIR os.chdir("/path/to/your/folder")


    # Uncomment to see what the Base Directory is, so you know the levels to add for the following paths
    print(f"Base Directory = {BASE_DIR}")

    image_dir = os.path.join(BASE_DIR, "Image_Holder", "Temp_Staging_Area")
    image_name = filename
    image_path = os.path.join(image_dir, image_name)

    # Change to Chamber folder: this is where the temporary data on pixel number in plants is saved
    temp_desktop_image_results = os.path.join(BASE_DIR, "Temp_Results", "temp_desktop_image_results.json")
    # Change to location where data from this run is saved
    analysis_results_csv_path = os.path.join(BASE_DIR, "Final_Data", "desktop_analysis_log.csv")
    # Change to location where scale_values is saved
    scale_values_path = os.path.join(BASE_DIR, "Pixels_to_mm", "scale_values.json")


    # In[3]:


    # Splits up plant name
    name_without_ext, _ = os.path.splitext(filename)
    print(name_without_ext)
    name_parts = name_without_ext.split('_')
    print(name_parts)


    # In[4]:


    # Input/output options
    args = WorkflowInputs(
        images=[image_path], # change to where the image will be
        names="image1",
        result=temp_desktop_image_results,
        outdir=".",
        writeimg=False,
        debug=None # set to "print" to just print steps, "plot" to see images at each step, None to not display any figures
        )


    # In[5]:


    # Set debug to the global parameter 
    pcv.params.debug = args.debug
    # Change display settings
    pcv.params.dpi = 100
    # Increase text size and thickness to make labels clearer
    # (size may need to be altered based on original image size)
    pcv.params.text_size = 10
    pcv.params.text_thickness = 20


    # In[6]:


    # Shows your image, defines it as "img"
    img, path, filename = pcv.readimage(filename=args.image1)


    # In[7]:


    # Crops your image
    crop_img = pcv.crop(img=img, x=845, y=220, h=1664, w=1653)


    # In[8]:


    # Shows options for which channel to view the image through (ideally want the most contrast)
    # colorspace_img = pcv.visualize.colorspaces(rgb_img=crop_img)


    # In[9]:


    # Actually picks a channel with rgb2gray_"lab" and then the channel is the letter from "lab" that you look through
    channeled_img = pcv.rgb2gray_lab(rgb_img=crop_img, channel='b')


    # In[10]:


    # Visualization only, not needed for analysis
    # hist_figure1, hist_data1 = pcv.visualize.histogram(img = channeled_img, hist_data=True)


    # In[11]:


    # Masks the image
    thresh_mask = pcv.threshold.binary(gray_img=channeled_img, threshold=130, object_type='light')


    # In[12]:


    # Deletes groups of pixels less than the pixel size (weird dots around edges not plant is unmasked)
    cleaned_mask = pcv.fill(bin_img=thresh_mask, size=420)


    # In[13]:


    # Defines Region of Interest (ROI) which selects white pixels and deselects black pixels from a masked image
    roi = pcv.roi.rectangle(img=cleaned_mask, x=110, y=200, h=500, w=1400)


    # In[14]:


    # Makes a new mask only with plants inside ROI

    # Inputs for the filtering function:
    #    mask            = the clean mask you made above
    #    roi            = the region of interest you specified above
    #    roi_type       = 'partial' (default, for partially inside the ROI then still keeps whole plant if some lies outside ROI), 'cutto' (hard cut off), or 
    #                     'largest' (keep only largest object)

    kept_mask  = pcv.roi.filter(mask=cleaned_mask, roi=roi, roi_type='partial')


    # In[15]:


    # Make new ROI's to select the different plants (use/change this for rows and columns of plants)
    auto_rois = pcv.roi.auto_grid(mask=kept_mask, nrows=1, ncols=4, img=crop_img)


    # In[16]:


    # Label and number objects in ROI; A good check to ensure different plants are different objects from being different colors
    labeled_mask, num_plants = pcv.create_labels(mask=kept_mask, rois=auto_rois, roi_type='partial')


    # In[17]:


    # Outputs analyzed image
    shape_image = pcv.analyze.size(img=crop_img, labeled_mask=labeled_mask, n_labels=num_plants)


    # In[18]:


    # Makes histogram of colors inside ROI
    # color_histogram = pcv.analyze.color(rgb_img=crop_img, labeled_mask=kept_mask, colorspaces='all', label="default")


    # In[19]:


    # Saves results for the 1 image (running again overwites past results)
    pcv.outputs.save_results(filename= args.result, outformat="json")


    # In[20]:


    # Gets pixels to mm scalar s (mm per pixel, so: pixels * s^2 = mm^2)
    with open(scale_values_path, "r") as f:
        scale_data = json.load(f)

    mean_s = scale_data["mean_scale_mm2_per_pixel"]
    std_s = scale_data["std_scale_mm2_per_pixel"]


    # In[21]:


    # Create single-row DataFrame and adds to analysis log
    for i in range(4):
        i = i+1
        pixels_value = pcv.outputs.observations[f"default_{i}"]["area"]["value"]
        new_data = pd.DataFrame([{
            "time": name_parts[2],
            "plant_number": f"plant{i}", 
            "plant_name": name_parts[0],
            "stress_level (%)": name_parts[1],
            "Area (mm^2)": pixels_value * mean_s,
            # "Uncertainty (mm^2)": pixels_value * 2 * mean_s * std_s
        }])
        # If analysis_log.csv doesn't exist, creates it with a header:
        if not os.path.isfile(analysis_results_csv_path):
            new_data.to_csv(analysis_results_csv_path, index=False)
        else:
            # Append without writing header again
            new_data.to_csv(analysis_results_csv_path, mode='a', header=False, index=False)


    # In[22]:


    # Moves image to longterm storage
    short_term_dir = os.path.join(BASE_DIR, "Image_Holder", "Temp_Staging_Area")
    long_term_dir = os.path.join(BASE_DIR, "Image_Holder", "Longterm_Storage")
    filename = image_name

    # Full paths
    src_path = os.path.join(short_term_dir, filename)
    dst_path = os.path.join(long_term_dir, filename)

    # Ensure long-term folder exists
    os.makedirs(long_term_dir, exist_ok=True)

    # Moves file to long-term folder
    shutil.move(src_path, dst_path)


    # In[23]:


    # plt.close('all')

def process_all_desktop_images():
    BASE_DIR = "/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj/Jupyter_Lab/WorkingVersion/Desktop_Version"
    image_dir = os.path.join(BASE_DIR, "Image_Holder", "Temp_Staging_Area")
    files = [f for f in os.listdir(image_dir) if not f.startswith(".")]
    if len(files) == 0:
        raise FileNotFoundError(f"No image files found in {image_dir}.")
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(image_dir, x)))
    print(f"Found {len(files)} images to process.\n")
    for i,filename in enumerate(files, start=1):
        print(f"({i}/{len(files)}) Processing image: {filename}")
        try:
            process_single_desktop_image(filename, BASE_DIR)
            print(f"Finished processing {filename}.\n")
        except Exception as e:
            print(f"Error processing {filename}: {e}\n")

if __name__ == "__main__":
    process_all_desktop_images()