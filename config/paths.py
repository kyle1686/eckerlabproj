import os

# Paths to base directories:


# Personal laptop changes these:
# To Github Repository:
GITHUB_REPO_PATH = '/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj'
# To Google Drive folder:
GOOGLE_DRIVE_FOLDER_PATH = '/Users/maxwellrosen/Library/CloudStorage/GoogleDrive-salkimager@gmail.com/My Drive'


analysis_results_csv_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'chamber_analysis_log.csv')
plant_mapping_csv_path = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'plant_names.csv')

# Chamber Left Paths:
cl_image_directory = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Holder')

# Tray 1 Paths:
t1_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray1')
t1_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray1_Plant_Pixels.json')
t1_temp_calibration_pixel_results = os.path.join(t1_github, 'Pixels_to_mm_T1', 'Tray1_Pixels_in_squares.json')
t1_scale_values_path = os.path.join(t1_github, 'Pixels_to_mm_T1', 'Tray1_scale_values.json')
t1_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Calibration', 'Tray1_Calibration')
t1_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray1', 'plant_names_t1.csv')
t1_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray1_analysis_log.csv')

# Tray 2 Paths:
t2_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray2')
t2_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray2_Plant_Pixels.json')
t2_temp_calibration_pixel_results = os.path.join(t2_github, 'Pixels_to_mm_T2', 'Tray2_Pixels_in_squares.json')
t2_scale_values_path = os.path.join(t2_github, 'Pixels_to_mm_T2', 'Tray2_scale_values.json')
t2_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Calibration', 'Tray2_Calibration')
t2_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray2', 'plant_names_t2.csv')
t2_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray2_analysis_log.csv')

# Tray 3 Paths:
t3_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray3')
t3_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray3_Plant_Pixels.json')
t3_temp_calibration_pixel_results = os.path.join(t3_github, 'Pixels_to_mm_T3', 'Tray3_Pixels_in_squares.json')
t3_scale_values_path = os.path.join(t3_github, 'Pixels_to_mm_T3', 'Tray3_scale_values.json')
t3_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CLeft_Calibration', 'Tray3_Calibration')
t3_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray3', 'plant_names_t3.csv')
t3_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray3_analysis_log.csv')

# Chamber Middle Paths:
cm_image_directory = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CMiddle_Holder')

# Tray 4 Paths:
t4_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray4')
t4_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray4_Plant_Pixels.json')
t4_temp_calibration_pixel_results = os.path.join(t4_github, 'Pixels_to_mm_T4', 'Tray4_Pixels_in_squares.json')
t4_scale_values_path = os.path.join(t4_github, 'Pixels_to_mm_T4', 'Tray4_scale_values.json')
t4_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CMiddle_Calibration', 'Tray4_Calibration')
t4_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray4', 'plant_names_t4.csv')
t4_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray4_analysis_log.csv')

# Tray 5 Paths:
t5_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray5')
t5_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray5_Plant_Pixels.json')
t5_temp_calibration_pixel_results = os.path.join(t5_github, 'Pixels_to_mm_T5', 'Tray5_Pixels_in_squares.json')
t5_scale_values_path = os.path.join(t5_github, 'Pixels_to_mm_T5', 'Tray5_scale_values.json')
t5_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CMiddle_Calibration', 'Tray5_Calibration')
t5_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray5', 'plant_names_t5.csv')
t5_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray5_analysis_log.csv')

# Chamber Right Paths:
cr_image_directory = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CRight_Holder')

# Tray 6 Paths:
t6_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray6')
t6_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray6_Plant_Pixels.json')
t6_temp_calibration_pixel_results = os.path.join(t6_github, 'Pixels_to_mm_T6', 'Tray6_Pixels_in_squares.json')
t6_scale_values_path = os.path.join(t6_github, 'Pixels_to_mm_T6', 'Tray6_scale_values.json')
t6_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CRight_Calibration', 'Tray6_Calibration')
t6_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray6', 'plant_names_t6.csv')
t6_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray6_analysis_log.csv')

# Tray 7 Paths:
t7_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray7')
t7_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray7_Plant_Pixels.json')
t7_temp_calibration_pixel_results = os.path.join(t7_github, 'Pixels_to_mm_T7', 'Tray7_Pixels_in_squares.json')
t7_scale_values_path = os.path.join(t7_github, 'Pixels_to_mm_T7', 'Tray7_scale_values.json')
t7_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CRight_Calibration', 'Tray7_Calibration')
t7_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray7', 'plant_names_t7.csv')
t7_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray7_analysis_log.csv')

# Tray 8 Paths:
t8_github = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray8')
t8_temp_pixel_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Temp_JSON_Pixel_Sizes', 'Tray8_Plant_Pixels.json')
t8_temp_calibration_pixel_results = os.path.join(t8_github, 'Pixels_to_mm_T8', 'Tray8_Pixels_in_squares.json')
t8_scale_values_path = os.path.join(t8_github, 'Pixels_to_mm_T8', 'Tray8_scale_values.json')
t8_calibration_image_path = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'CRight_Calibration', 'Tray8_Calibration')
t8_plant_names = os.path.join(GITHUB_REPO_PATH, 'On_Laptop', 'Chamber', 'Tray8', 'plant_names_t8.csv')
t8_analysis_results = os.path.join(GOOGLE_DRIVE_FOLDER_PATH, 'Chamber', 'Final_Data', 'tray8_analysis_log.csv')


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

## Maybe usless for now?
# Chamber Left (cl) Paths:
cl_repo_root = '/home/user2/Salk_Project_Folder/eckerlabproj'
cl_image_save_path = '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Holder'
cl_gdrive_remote_path = 'gdrive:Chamber/CLeft_Holder'
cl_t1_calibimage_save_path =  '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Calibration/Tray1_Calibration'
cl_t2_calibimage_save_path = '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Calibration/Tray2_Calibration'
cl_t3_calibimage_save_path = '/home/user2/Salk_Project_Folder/Google_Drive/CLeft_Calibration/Tray3_Calibration'
cl_gdrive_calibration_path = 'gdrive:Chamber/CLeft_Calibration'

# Chamber Middle (cm) Paths:
cm_repo_root = '/home/chamberuser1/Salk_Project_Folder/eckerlabproj'
cm_image_save_path = '/home/chamberuser1/Salk_Project_Folder/Google_Drive/CMiddle_Holder'
cm_gdrive_remote_path = 'gdrive:Chamber/CMiddle_Holder'
cm_t4_calibimage_save_path =  '/home/chamberuser1/Salk_Project_Folder/Google_Drive/CMiddle_Calibration/Tray4_Calibration'
cm_t5_calibimage_save_path = '/home/chamberuser1/Salk_Project_Folder/Google_Drive/CMiddle_Calibration/Tray5_Calibration'
cm_gdrive_calibration_path = 'gdrive:Chamber/CMiddle_Calibration'

# Chamber Right (cr) Paths:
cr_repo_root = '/home/user300/Salk_Project_Folder/eckerlabproj'
cr_image_save_path = '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Holder'
cr_gdrive_remote_path = 'gdrive:Chamber/CRight_Holder'
cr_t6_calibimage_save_path =  '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Calibration/Tray6_Calibration'
cr_t7_calibimage_save_path = '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Calibration/Tray7_Calibration'
cr_t8_calibimage_save_path = '/home/user300/Salk_Project_Folder/Google_Drive/CRight_Calibration/Tray8_Calibration'
cr_gdrive_calibration_path = 'gdrive:Chamber/CRight_Calibration'
