import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, destination_dir):
    
    if not os.path.exists(source_dir):                                      #Check if source directory exists
        print(f"Error: Source directory '{source_dir}' does not exist.")
        sys.exit(1)
    
    if not os.path.exists(destination_dir):                                 #Check if destination directory exists; if not, create it
        print(f"Destination directory '{destination_dir}' does not exist. Creating it.")
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):                                 #Iterate through files in the source directory
        source_file = os.path.join(source_dir, filename)
        
        if os.path.isfile(source_file):                                     #Check if it's a file (not a directory)
            destination_file = os.path.join(destination_dir, filename)      #Determine destination file path
            
            if os.path.exists(destination_file):                            #If destination file already exists, create a unique filename
                base, extension = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                destination_file = os.path.join(destination_dir, f"{base}_{timestamp}{extension}")
            
            shutil.copy2(source_file, destination_file)                     #Copy file to the destination directory
            print(f"Copied '{source_file}' to '{destination_file}'")

if __name__ == "__main__":

    if len(sys.argv) != 3:                                                  #Check for command-line arguments
        print("""\n     No argument found. 
            - Please provide source and destination directory  : 
            - python backup.py /path/to/source /path/to/destination\n""")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    
    backup_files(source_directory, destination_directory)       #backup fuction