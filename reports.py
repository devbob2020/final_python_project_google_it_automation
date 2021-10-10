#!/usr/bin/python3

#import os
#import re
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

def generate_report(paragraph, title, attachment):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])

    report_table = Table(data=paragraph, hAlign="LEFT")
    report.build([report_title, report_table])
