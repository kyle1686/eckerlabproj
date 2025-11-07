import os

# Paths to base directories:


# Personal laptop changes these:
# To Github Repository:
GITHUB_REPO_PATH = '/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj'
# To Google Drive folder:
GOOGLE_DRIVE_FOLDER_PATH = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive'

t1_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Calibration', 'Tray1_Calibration')


# Chamber Left (cl) Paths:
cl_repo_root = '/home/user2/Salk_Project_Folder/eckerlabproj'
cl_image_save_path = '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Holder'
cl_gdrive_remote_path = 'gdrive:Chamber'
cl_t1_calibimage_save_path =  '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Calibration/Tray1_Calibration'
cl_t2_calibimage_save_path = '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Calibration/Tray2_Calibration'
cl_t3_calibimage_save_path = '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Calibration/Tray3_Calibration'

# Chamber Middle (cm) Paths:
cm_repo_root = '/home/chamberuser1/Salk_Project_Folder/eckerlabproj'
cm_image_save_path = '/home/chamberuser1/Salk_Project_Folder/Google_Drive/CMiddle_Holder'
cm_gdrive_remote_path = 'gdrive:Chamber'
cm_t4_calibimage_save_path =  '/home/chamberuser1/Salk_Project_Folder/Google_Drive/CMiddle_Calibration/Tray4_Calibration'
cm_t5_calibimage_save_path = '/home/chamberuser1/Salk_Project_Folder/Google_Drive/CMiddle_Calibration/Tray5_Calibration'

# Chamber Right (cr) Paths:
cr_repo_root = '/home/user300/Salk_Project_Folder/eckerlabproj'
cr_image_save_path = '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Holder'
cr_gdrive_remote_path = 'gdrive:Chamber'
cr_t6_calibimage_save_path =  '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Calibration/Tray6_Calibration'
cr_t7_calibimage_save_path = '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Calibration/Tray7_Calibration'
cr_t8_calibimage_save_path = '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Calibration/Tray8_Calibration'



# Processing Paths:
analysis_results_csv_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'chamber_analysis_log.csv')
plant_mapping_csv_path = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'plant_names.csv')

# Chamber Left Paths:
cl_image_directory = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Holder')

# Tray 1 Paths:
t1_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray1_Pixels.json')
t1_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray1_scale_values.json')
t1_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Calibration', 'Tray1_Calibration')

# Tray 2 Paths:
t2_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray2_Pixels.json')
t2_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray2_scale_values.json')

# Tray 3 Paths:
t3_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray3_Pixels.json')
t3_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray3_scale_values.json')

# Chamber Middle Paths:
cm_image_directory = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CMiddle_Holder')

# Tray 4 Paths:
t4_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray4_Pixels.json')
t4_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray4_scale_values.json')

# Tray 5 Paths:
t5_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray5_Pixels.json')
t5_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray5_scale_values.json')

# Chamber Right Paths:
cr_image_directory = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CRight_Holder')

# Tray 6 Paths:
t6_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray6_Pixels.json')
t6_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray6_scale_values.json')

# Tray 7 Paths:
t7_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray7_Pixels.json')
t7_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray7_scale_values.json')

# Tray 8 Paths:
t8_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray8_Pixels.json')
t8_scale_values_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Scale_Values', 'Tray8_scale_values.json')



TEMP_CHAMBER_IMAGE_RESULTS = "./On_Laptop/Chamber_Jupyter_Labs/Chamber1/temp_chamber_image_results.json"

SCALE_VALUE_PATH = "./On_Laptop/Chamber_Jupyter_Labs/Chamber1/Pixels_to_mm_C1/scale_values.json"
PLANT_NAMES_PATH = "./On_Laptop/Chamber_Jupyter_Labs/plant_names.csv"

# for below, may need to modify / add a directory on the github for data eventually

ANALYSIS_RESULTS_CSV_PATH = "/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Final_Data/chamber_analysis_log.csv"

# SHORT_TERM_DIR is also known as IMAGE_DIR
SHORT_TERM_DIR1 = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Temp_C1_Holder'
SHORT_TERM_DIR2 = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Temp_C2_Holder'
LONG_TERM_DIR = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber/Longterm_Image_Storage'

CHAMBER_BASE_DIR = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Chamber'
DESKTOP_BASE_DIR = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive/Desktop'