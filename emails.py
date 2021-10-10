#!/usr/bin/python3

import os.path
import mimetypes
import smtplib
import getpass
from email.message import EmailMessage

###############################################################
# variable list which must be filled in before program is run #
###############################################################

web_address = '192.168.1.214'

###############################################################

def generate_email(sender, receiver, subject, body, attachment):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)
    if attachment != "":
        attachment_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment, 'rb') as ap:
            message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment))
    return message

def send_email(sender, receiver, password, message):
    try:
        mail_server = smtplib.SMTP(web_address)
        #mail_server = smtplib.SMTP_SSL(ip_address)
        #mail_server.login(sender, password)
        mail_server.send_message(message)
        mail_server.quit()
    except:
        print("Error: Can't send email")
