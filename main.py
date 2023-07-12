import os
import glob

# Root directory
root_dir = r"C:\Users\Dana\Desktop\Goats"

# Iterate over all subdirectories in the root directory
for subdir in os.listdir(root_dir):
    # Generate the full path to the subdirectory
    subdir_full = os.path.join(root_dir, subdir)

    # Check that it's actually a directory
    if os.path.isdir(subdir_full):
        # Use glob to find all PNG files in the subdirectory
        for file_path in glob.glob(os.path.join(subdir_full, "*.png")):
            # Get the base name of the file (without the directory)
            file_name = os.path.basename(file_path)

            # Check if the file name starts with 'm' and the length is greater than or equal to 13
            if file_name.startswith('m') and len(file_name) >= 13:
                # Extract the SKU from the file name
                sku = file_name[:13]

                # Construct the new name by appending the directory name (removing spaces and replacing them with '-')
                # and '.png'
                new_name = sku + "_" + subdir.replace(" ", "-") + ".png"

                # Generate the full path to the new file
                new_file_path = os.path.join(subdir_full, new_name)

                # Rename the file
                os.rename(file_path, new_file_path)
