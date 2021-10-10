#!/usr/bin/python3

import os
import datetime
#import re
import reports
import emails
#from reportlab.platypus import SimpleDocTemplate
#from reportlab.platypus import Paragraph, Spacer, Table, Image
#from reportlab.lib.styles import getSampleStyleSheet
import datetime

###############################################################
# variable list which must be filled in before program is run #
###############################################################

sender = 'vm@localserver.com'
receiver = 'admin@localserver.com'
subject = 'Upload Completed - Online Fruit Store'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment = '/tmp/processed.pdf'
password = 'sesame'
path = 'supplier-data/descriptions/'

###############################################################

paragraph = ''
date = datetime.datetime.today()
title = "Processed Update on " + str(date.strftime("%B") + " " + str(date.day) + ", " + str(date.year))
posts = []
directories = os.listdir(path)
table_data = []
count = 0

# cycle thru files and get fruit name and weight info and stick it in a 'post' list
for filename in directories:
    file = os.path.join(path, filename)
    with open(file, 'r') as f:
        base = os.path.basename(file)
        name, ext = os.path.splitext(base)
        img_name = name + '.jpeg'
        posts.append({"name":f.readline().strip(),
        "weight":f.readline().strip()})

table_data.append(["\n"])
for element in posts:
    for key, value in element.items():
        key = key + ":"
        table_data.append([key, value])
        count += 1
        #print(count, "   ", key, "   ", value)\
    if count % 2 == 0:
        table_data.append([" "])

if __name__ == "__main__":
    reports.generate_report(table_data, title, attachment)
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(sender, receiver, password, message)
    
