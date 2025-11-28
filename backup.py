from datetime import datetime
import os
import shutil
import sys

def backup_files(source_dir, dest_dir):
    # Check if source & destination directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
  
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return
    
    for file in os.listdir(source_dir):
     src_path = os.path.join(source_dir, file)
     if os.path.isfile(src_path):  # Only copy files
      dest_path = os.path.join(dest_dir, file)

        # If file exists, add timestamp
      if os.path.exists(dest_path):
            name, ext = os.path.splitext(file)
            time = datetime.now().strftime("%Y%m%d_%H%M%S")
            file = f"{name}_{time}{ext}"
            dest_path = os.path.join(dest_dir, file)
    
      try:
        shutil.copy2(src_path, dest_path)
        print(f"Copied: {file} -> {dest_path}")
      except Exception as e:
        print(f"Failed to copy '{file}': {e}")

# ---- MAIN SCRIPT ----
if __name__ == "__main__":
    print('Usage: python backup.py <source_directory> <destination_directory>:')
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    backup_files(source_dir,dest_dir)
