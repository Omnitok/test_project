#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:33:52 2023
Converting 'tif', 'tiff' and 'pgm' to 'png'
@author: Stenszky János
"""
from tqdm import tqdm
from PIL import Image
import os

def convert_pgm_to_png(tif_file, png_file):
    with Image.open(tif_file) as im:
        im.save(png_file)

# Folder path containing the TIF files
folder_path = input('Input folder:')

# Output folder for PNG files
output_folder = input('Output folder:')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all files in the input folder
files = os.listdir(folder_path)

# Define a list of file extensions you want to handle
file_extensions = ['.tif', '.tiff', '.pgm']

# Initialize a tqdm progress bar
progress_bar = tqdm(total=len(files), desc='Converting Images')

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    for extension in file_extensions:
        if filename.endswith(extension):
        # Construct input and output file paths
            og_file = os.path.join(folder_path, filename)
            png_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

        # Convert PGM to PNG
            convert_pgm_to_png(og_file, png_file)
            
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()


print('Conversion complete. Images saved in', output_folder)
