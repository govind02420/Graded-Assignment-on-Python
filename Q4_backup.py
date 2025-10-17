import os
import shutil
import sys
import time

def backup_files(src_dir, dest_dir):
    """
    Copy all files from source to destination directory.
    - If a file with the same name exists, append a timestamp to avoid overwriting.
    - Handles errors gracefully if directories are missing.
    """
    # Check if source and destination directories exist
    if not os.path.exists(src_dir):
        print(f"❌ Source directory not found: {src_dir}")
        return
    if not os.path.exists(dest_dir):
        print(f"❌ Destination directory not found: {dest_dir}")
        return

    # Iterate through files in source directory
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)

        # Process only regular files (ignore folders)
        if os.path.isfile(src_file):
            # If destination file exists, add timestamp
            if os.path.exists(dest_file):
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                name, ext = os.path.splitext(filename)
                dest_file = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")

            # Copy file with metadata
            shutil.copy2(src_file, dest_file)
            print(f"✅ Backed up: {filename} → {dest_file}")


if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
        sys.exit(1)

    src = sys.argv[1]
    dest = sys.argv[2]

    # Start backup process
    backup_files(src, dest)
