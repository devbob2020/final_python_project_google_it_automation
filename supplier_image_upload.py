#!/usr/bin/python3

import requests
#import os
from pathlib import Path

###############################################################
# variable list which must be filled in before program is run #
###############################################################

url = "http://localhost/upload/"
path = '/home/<home directory goes here>/supplier-data/images/'

###############################################################

dir = Path(path).glob('*')
for item in dir:
    print(item)
    if Path(item).suffix == '.jpeg':
        with open(item, 'rb') as opened:
            r = requests.post(url, files={'file':opened})
