#!/usr/bin/python3

import os
from PIL import Image
from pathlib import Path

###############################################################
# variable list which must be filled in before program is run #
###############################################################

path = 'supplier-data/images/'

###############################################################

files = Path(path).glob('*')
for file in files:
    if str(Path(file).suffix) == '.tif' or str(Path(file).suffix) == '.tiff':
        print(file)
        rgb_filename = Path(file).stem + '.jpeg'
        rgba_img = Image.open(file)
        rgb_img = rgba_img.convert('RGB')
        rgb_img = rgb_img.resize((600, 400))
        rgb_img.save(os.path.join(path, rgb_filename))
