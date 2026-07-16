# Legacy

Older code kept for reference, not part of the current workflow.

- **`batch_process_template.py`** — a barebones, generic batch-processing script,
  cleaned up from the original whole-chamber batch drivers
  (`Process_all_Chamber1_images.py`, `Process_all_Chamber2_images.py`,
  `Process_Whole_Chamber.py`, which predate the per-tray restructure and are still in
  the git history). It processes every image in a folder in one run: crop → mask →
  one ROI per pot → measure area → convert to mm² → append to a CSV → move the image.

  Fill in the `EDIT ME` values and adapt the mask/ROI section to your layout, then run
  `python batch_process_template.py`.

Batch processing only works well when imaging conditions are stable across the whole
run — the tray stays put (so one crop stays valid), plants stay green and don't touch,
and the ROIs don't need adjusting between images. When conditions need per-image
attention (re-cropping, re-tuning), use the per-tray `Process_TrayN.ipynb` notebooks
instead.
