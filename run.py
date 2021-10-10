#! /usr/bin/python3

import os
import re
import requests

###############################################################
# variable list which must be filled in before program is run #
###############################################################

path = 'supplier-data/descriptions/'
url = 'http://<ip address goes here>/fruits/'

###############################################################

posts = []
directories = os.listdir(path)

for filename in directories:
    file = os.path.join(path, filename)
    with open(file, 'r') as f:
        base = os.path.basename(file)
        name, ext = os.path.splitext(base)
        img_name = name + '.jpeg'
        posts.append({"name":f.readline().strip(),
        "weight":re.search(r"(\d*)(\s\S*)", f.readline().strip())[1],
        "description":f.readline().strip(),
        "image_name":img_name.strip()})

for post in posts:
    response = requests.post(url, json=post)
#    if response.status_code != 201:
#        raise Exception('Error: HTTP Status = {}'.format(response.status_code))
