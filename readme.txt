This project is the solution to the final capstone project lab 
"Automate updating catalog information" in the online coursera.org 
class called "Google IT Automation with Python". These files 
should be run in a linux environment. Some of the files 
can't be used outside the lab setup. You can, however, run:

$./changeImage.py 		# this changes the image files in  c
                               # "supplier-data/images" from .tif
                               # files with 3000x2000 px resolution
                               # to .jpeg files with 600x400 px 
                               # resolution

$(can't successfully run "./suppier_image_upload.py" outside of lab environment)

$(can't successfully run "./run.py" outside of lab environment )

$(do not run "./reports.py" or "./emails.py" by themselves. They are used by "./report_email.py")

$./report_email.py		# this script uses reports.py and 
				# emails.py and creates a report 
				# in pdf format, putting a copy at:
				# /tmp/processed.pdf (or place of 
				# your choice) and generating and 
				# sending an email to the address 
				# of your choice and attaching a
				# report with the 'processed.pdf'
				# file.
				
$./health_check.py		# this file can be run as a cron job
				# at regular intervals. It monitors 
				# system resources and sends out an 
				# email alert when cpu usage is too 
				# high or when disk usage is too high
				# or when available memory is too low.
				# Also sends an alert if 'localhost' 
				# does not resolve to: 127.0.0.1
				







