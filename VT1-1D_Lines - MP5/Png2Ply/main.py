import png2ply
import os
import sys
import shutil

# Manually define the arguments here
SOURCE_DIR = r"C:/Users/victo/OneDrive - Aalborg Universitet/Skrivebord/5. Semester/P5 projekt/Scanner/VT1-1D_Lines - MP5/Png2Ply/Insert_Images"
TARGET_DIR = r"C:/Users/victo/OneDrive - Aalborg Universitet/Skrivebord/5. Semester/P5 projekt/Scanner/VT1-1D_Lines - MP5/PointClouds"
SAVE_RGB = True  # Set to True if you want to save in RGB format
SAVE_TRIANGLES = True  # Set to True if you want to save triangles

###################################
##      DELETE OLD POINTCLOUDS   ##
###################################

# Specify the folder
folder_path = TARGET_DIR

# Safely delete all contents
try:
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # Deletes the folder and all its contents
        print(f"Successfully deleted the folder and its contents: {folder_path}")
    else:
        print(f"The folder does not exist: {folder_path}")

    # Recreate the folder
    os.makedirs(folder_path, exist_ok=True)
    print(f"Recreated the folder: {folder_path}")

except PermissionError as e:
    print(f"PermissionError: Unable to delete folder. {e}")
except OSError as e:
    print(f"OSError: {e}")

#

# Check if directories exist
if not (os.path.isdir(SOURCE_DIR)):
    sys.exit("Source directory was not found.")
if not os.path.isdir(TARGET_DIR):
    os.makedirs(TARGET_DIR)

print(f"Saving PLY files in {TARGET_DIR}")

# Go through all PNG files in source directory
for file in os.listdir(SOURCE_DIR):
    filename = os.fsdecode(file)
    if filename.endswith(".png") or filename.endswith(".PNG"):
        source_file = f"{SOURCE_DIR}/{filename}"
        target_file = f"{TARGET_DIR}/{filename[:-4]}.ply"
        converter = png2ply.Png2PlyConverter(source_file, target_file)
        converter.extract_data()
        converter.write_ply(SAVE_RGB, SAVE_TRIANGLES)
        continue
    else:
        continue

print('Done')
