"""
Project conventions and formatting reference.

This file documents the naming and formatting conventions used across the
repository. It is a reference, not runtime configuration -- actual machine
paths live in `config/paths.py`. Keeping the conventions in one place makes it
easy for a new person to see the patterns the rest of the code follows.
"""

# ---------------------------------------------------------------------------
# Timestamp formats
# ---------------------------------------------------------------------------
# Routine capture images are stamped to the minute; anything needing seconds
# (e.g. calibration shots taken in quick succession) adds seconds. Both are
# sortable as plain strings, which is what the processing and video notebooks
# rely on to order frames in time.
TIME_FORMAT = "%Y-%m-%d--%H-%M"                   # e.g. 2025-12-23--13-00
TIME_FORMAT_WITH_SECONDS = "%Y-%m-%d--%H-%M-%S"   # e.g. 2025-12-23--13-00-45


# ---------------------------------------------------------------------------
# Filename formats
# ---------------------------------------------------------------------------
# Capture images:      Chamber{Position}_image_{timestamp}.jpg
#   Position is one of: Left, Middle, Right
#   e.g. ChamberLeft_image_2025-12-23--13-00.jpg
IMAGE_FILENAME_FORMAT = "Chamber{position}_image_{timestamp}.jpg"

# Calibration images:  Tray{n}_calibration_image_{timestamp}.jpg
CALIBRATION_FILENAME_FORMAT = "Tray{n}_calibration_image_{timestamp}.jpg"

# Per-tray data files kept in the repo:
#   plant_names_t{n}.csv             maps pot position -> genotype for tray n
#   Tray{n}_scale_values.json        pixels-to-mm scale for tray n
#   Tray{n}_Pixels_in_squares.json   calibration square pixel counts for tray n


# ---------------------------------------------------------------------------
# Folder structure
# ---------------------------------------------------------------------------
# Repo (code + small config/data only; images are never committed):
#   On_Pi/       Raspberry Pi capture scripts, one folder per camera
#   On_Laptop/   analysis notebooks, run on the lab computer
#   config/      path configuration (edit paths.py per machine)
#
# Google Drive (shared image + data store):
#   Chamber/C{Left,Middle,Right}_Holder/Tray{n}_Holder/   incoming images
#   Chamber/C{Left,Middle,Right}_Calibration/             calibration per camera
#   Chamber/Final_Data/tray{n}_analysis_log.csv           processed output
#   Chamber/Longterm_Image_Storage/                       archived raw images


# ---------------------------------------------------------------------------
# Path style
# ---------------------------------------------------------------------------
# All machine-specific paths are built in `config/paths.py` from two base paths
# set once per machine, then imported everywhere via `import config.paths`.
# Never hard-code a full path in a notebook -- add it to config/paths.py so the
# whole pipeline moves to a new machine by editing only those two base values.
#
#   GITHUB_REPO_PATH         = "<lab computer's path to the cloned repo>"
#   GOOGLE_DRIVE_FOLDER_PATH = "<lab computer's path to the synced Google Drive>"


# ---------------------------------------------------------------------------
# Analysis CSV columns
# ---------------------------------------------------------------------------
ANALYSIS_CSV_COLUMNS = [
    "time",
    "date",
    "Tray Number",
    "plant_number",
    "plant_spec",
    "plant_ID",
    "Area (mm^2)",
    "Stress (%)",
]
