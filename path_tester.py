import sys
# Change to repository root, so it can find the config folder with the paths inside it
repo_root = '/Users/maxwellrosen/Storage/Salk_Plant_Imaging/eckerlabproj'
# Add config folder with paths to Python's import search path
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import config.paths as paths

print(paths.chamber_left_image_save_path)