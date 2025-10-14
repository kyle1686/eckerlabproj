# Crontab Controls

This document explains how the Raspberry Pi automatically captures images using a scheduled task managed by **crontab**

## What is Crontab?

**Crontab** (a.k.a. cron table) is a configuration file for scheduling commands to run automatically at specific times on Unix-based systems like the Raspberry Pi. 

Each line in the crontab represents a job and follows the following structure:

```
\* \* \* \* \* command_to_run
| | | | |
| | | | |_Day of week (0-6, Sunday = 0)
| | | |____Month (1-12)
| | |_______Day of month (1-31)
| |__________Hour(0-23)
|_____________Minute(0-59)
```

Here's a great resource for understanding/making your automation: https://crontab.guru/

## Image Capture Schedule

Here's an example of running the python code to capture images automatically throughout the day:
`*/20 10-18 * * * /usr/bin/python3 /home/user/your-repo-name/takepicture.py`

### Explanation:
- "*/20" → Runs every **20 minutes**
- "10-18" → Runs between **10 AM and 6 PM**
- "\* \* \*" → Every day of every month
- "/usr/bin/python3" → The path to the Python 3 interpreter (to find your specific path, type "which python3" into your Raspberry Pi terminal, and it'll tell you the path, and you should use that in this location)
- "/home/user/your-repo-name/takepicture.py" → The script that captures the image

---

## Useful Commands

How to edit your crontab (change automated commands):
1. Open crontab editor (if it's your first time, enter "1" for the easiest editor):
```
crontab -e
```
2. Scroll to the bottom (using the down arrow key)
3. Add your cron job line (see example above)
4. Once finished, press Ctrl + O → Press Enter to save, and Ctrl + X to exit nano
5. Check that it saved - to see crontab, type the following and you should see your new line listed:
```
crontab -l
```

How to check if cron is running:
1. Type this into the terminal: 
```
sudo systemctl status cron
```
2. You should see "active (running)" somewhere
3. Once done looking at it, type "q" to exit the status view