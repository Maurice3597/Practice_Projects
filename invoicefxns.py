import os
import time

FOLDER_NAME = 'invoice_pdf'


def home_dir():
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

def create_time():
     date = time.strftime("Date: %d/%m/%y")
     return date
