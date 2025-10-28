from Process_Chamber1 import process_Chamber1
from Process_Chamber2 import process_Chamber2

# Make sure to have run the scale value calibration first before using this script

def run_all():
    process_Chamber1()
    process_Chamber2()
    
if __name__ == "__main__":
    run_all()