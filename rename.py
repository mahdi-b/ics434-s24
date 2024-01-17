import os

def rename_files_in_directory(directory="."):
    # Get the list of files in the specified directory
    files = os.listdir(directory)

    # Loop through each file
    for file in files:
        # Check if the file ends with ".ipynb"
        if file.endswith(".ipynb"):
            # Split the file name by "_"
            parts = file[:-6].split("_")  # Removing ".ipynb" and then splitting
            if len(parts) > 0:
                # Check if the first part is a number
                if parts[0].isdigit():
                    # Check if it's a single-digit number
                    if len(parts[0]) == 1:
                        # Append a "0" in front of the file name
                        new_name = "0" + file
                        # Construct the full paths
                        old_path = os.path.join(directory, file)
                        new_path = os.path.join(directory, new_name)
                        # Rename the file
                        os.rename(old_path, new_path)
                        print(f'Renamed: {file} -> {new_name}')

# Call the function with the current directory as the default
rename_files_in_directory()

