#!/usr/bin/python3

import os
import psutil
import shutil
import smtplib
import getpass
import time
import socket
import emails
from email.message import EmailMessage

body = "Please check your system and resolve the issue as soon as possible."
cpu_alert = "Error - CPU usage is over 80%"
disk_alert = "Error - Available disk space is less than 20%"
mem_alert = "Error - Available memory is less than 500MB"
host_alert = "Error - localhost cannot be resolved to 127.0.0.1"
attachment = ""

###############################################################
# variable list which must be filled in before program is run #
###############################################################

password = 'sesame'
sender = 'vm@localserver.com'
receiver = 'admin@localserver.com'

###############################################################

def get_pc_status():
    try:
        cpu_usage = psutil.cpu_percent(4)
        disk_usage = psutil.disk_usage('/')
        disk_percent = float(disk_usage.used)/float(disk_usage.total)*100
        disk_percent = "{:.2f}".format(disk_percent)
        disk_percent = float(disk_percent)
        mem_stats = psutil.virtual_memory()
        mem_left = mem_stats[1]
    except:
        print("Error: Can't get PC status")
    return [cpu_usage, disk_percent, mem_left]

def get_ip():
    try:
        ip_address = socket.gethostbyname('localhost')
        return ip_address
    except:
        print("Error: Can't get IP address")

cpu_usage, disk_percent, mem_left = get_pc_status()

if cpu_usage > 80.0:
    message = emails.generate_email(sender, receiver, cpu_alert, body, attachment)
    emails.send_email(sender, receiver, password, message)

if disk_percent < 0.2:
    message = emails.generate_email(sender, receiver, disk_alert, body, attachment)
    emails.send_email(sender, receiver, password, message)

if mem_left > 500000000:
    message = emails.generate_email(sender, receiver, mem_alert, body, attachment)
    emails.send_email(sender, receiver, password, message)

if get_ip() != '127.0.0.1':
    message = emails.generate_email(sender, receiver, host_alert, body, attachment)
    emails.send_email(sender, receiver, password, message)
