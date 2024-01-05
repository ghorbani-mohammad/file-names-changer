import os
import re


# Get the current working directory (where the script is executing)
directory_path = os.getcwd()

# Get a list of all files in the directory
file_list = os.listdir(directory_path)

# Filter the list to include only files with the specified extension (e.g., .mp4)
file_list = [file for file in file_list if file.endswith('.mp4')]

# Rename the files with the reversed date order
for filename in file_list:
    if "IELTS" not in filename:
        continue

    date_pattern = r"\d{2}\.\d{2}\.\d{4}"
    dates = re.findall(date_pattern, filename)
    parts = dates[0].split('.')
    day, month, year = parts

    extension = filename.split('.')[-1]

    new_filename = f"{year}.{month}.{day}.{extension}"
    os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
