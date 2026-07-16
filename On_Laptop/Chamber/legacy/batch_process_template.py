"""
Legacy batch-processing template (barebones, adapt-me).

This is a cleaned-up, generic version of the old whole-chamber batch scripts that
predate the per-tray restructure. It is NOT wired into the current pipeline -- it is
a starting point you can copy and adapt.

The supported day-to-day workflow is the per-tray `Process_TrayN.ipynb` notebooks,
which let you re-crop and re-tune the mask and ROIs for each tray. Automated batch
processing like this only works well when imaging conditions are stable across the
whole run: the tray doesn't move (so one crop stays valid), plants stay green and
don't touch, and the ROIs don't need adjusting between images. When that holds, this
loop lets you process a whole folder of images in one command with no manual
intervention. When it doesn't, use the per-tray notebooks instead.

To use it: fill in every value marked `EDIT ME`, adapt the mask/ROI section to your
layout, and run `python batch_process_template.py`.
"""

import os
import json
import shutil

import pandas as pd
from plantcv import plantcv as pcv
from plantcv.parallel import WorkflowInputs


# --- EDIT ME: paths --------------------------------------------------------
IMAGE_DIR       = "<folder of images to process>"           # e.g. .../Chamber/CLeft_Holder/Tray1_Holder
DONE_DIR        = "<folder to move processed images into>"  # e.g. .../Chamber/Longterm_Image_Storage
SCALE_VALUES    = "<path to TrayN_scale_values.json>"       # produced by the pixels_to_mm notebook
PLANT_NAMES_CSV = "<path to plant_names.csv>"               # columns: old_plant_number, new_name, stress
OUTPUT_CSV      = "<path to the output analysis_log.csv>"
TEMP_RESULTS    = "temp_results.json"                       # scratch file PlantCV writes per image

# --- EDIT ME: imaging parameters -------------------------------------------
CROP       = dict(x=0, y=0, w=1773, h=1769)   # crop box around the tray of plants
THRESHOLD  = 127                              # LAB 'a'-channel threshold (dark = plant)
FILL_SIZE  = 100                              # smallest blob to keep (removes speckle noise)
ROI_RADIUS = 40                               # radius of each per-plant region of interest
ROI_COORDS = [                                # one (x, y) centre per pot, in crop coordinates
    # (159, 155), (361, 132), ...  <- paste your pot centres here
]


def process_image(filename):
    """Process one image: mask, measure each plant, append rows to OUTPUT_CSV."""
    image_path = os.path.join(IMAGE_DIR, filename)

    # Filenames look like Chamber{Pos}_image_YYYY-MM-DD--HH-MM.jpg; pull out the timestamp.
    time = os.path.splitext(filename)[0].split("_")[-1]

    args = WorkflowInputs(images=[image_path], names="image", result=TEMP_RESULTS,
                          outdir=".", writeimg=False, debug=None)
    pcv.params.debug = args.debug

    img, _, _ = pcv.readimage(filename=args.image)
    crop_img = pcv.crop(img=img, x=CROP["x"], y=CROP["y"], w=CROP["w"], h=CROP["h"])

    # Mask on the LAB 'a' channel (green tissue vs. soil), then clean up the mask.
    channeled = pcv.rgb2gray_lab(rgb_img=crop_img, channel="a")
    thresh = pcv.threshold.binary(gray_img=channeled, threshold=THRESHOLD, object_type="dark")
    mask = pcv.fill(bin_img=thresh, size=FILL_SIZE)

    # One region of interest per pot, then measure the plant inside each.
    rois = pcv.roi.multi(img=mask, coord=ROI_COORDS, radius=ROI_RADIUS)
    labeled_mask, n_plants = pcv.create_labels(mask=mask, rois=rois, roi_type="partial")
    pcv.analyze.size(img=crop_img, labeled_mask=labeled_mask, n_labels=n_plants)
    pcv.outputs.save_results(filename=args.result, outformat="json")

    # Convert pixel area to mm^2 using the tray's scale, and attach genotype names.
    with open(SCALE_VALUES) as f:
        mean_s = json.load(f)["mean_scale_mm_per_pixel"]
    names = pd.read_csv(PLANT_NAMES_CSV)

    for i in range(1, len(ROI_COORDS) + 1):
        pixels = pcv.outputs.observations[f"default_{i}"]["area"]["value"]
        plant_number = f"plant{i}"
        row = names.loc[names["old_plant_number"] == plant_number]
        new_row = pd.DataFrame([{
            "time": time,
            "plant_number": plant_number,
            "plant_ID": row["new_name"].values[0],
            "Area (mm^2)": pixels * (mean_s ** 2),
            "Stress (%)": row["stress"].values[0],
        }])
        header = not os.path.isfile(OUTPUT_CSV)
        new_row.to_csv(OUTPUT_CSV, mode="a", header=header, index=False)

    # Move the processed image out of the incoming folder so it isn't counted twice.
    os.makedirs(DONE_DIR, exist_ok=True)
    shutil.move(image_path, os.path.join(DONE_DIR, filename))


def process_all():
    files = [f for f in os.listdir(IMAGE_DIR) if not f.startswith(".")]
    if not files:
        raise FileNotFoundError(f"No images found in {IMAGE_DIR}.")
    files.sort(key=lambda f: os.path.getmtime(os.path.join(IMAGE_DIR, f)))
    print(f"Found {len(files)} images to process.")
    for i, filename in enumerate(files, start=1):
        print(f"({i}/{len(files)}) {filename}")
        try:
            process_image(filename)
        except Exception as e:
            print(f"  error on {filename}: {e}")
    print("Done.")


if __name__ == "__main__":
    process_all()
