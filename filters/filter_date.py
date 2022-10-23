from pickle import FALSE, TRUE
import sys
import json
import time
import datetime
from datetime import date

def filter_date(image_datetime, today_idc):
    today_date = date.today().strftime("%Y/%m/%d")
    # today_date = time.strptime(today_date, "%d/%m/%Y")
    print(str(today_date))
    image_date = str(image_datetime[0:10])
    created_date = datetime.datetime.strptime(image_date, '%Y-%m-%d').strftime("%Y/%m/%d")
    # created_date = time.strptime(created_date, "%d/%m/%Y")
    # created_date = datetime.datetime.strftime(image_date, "%d/%m/%Y")
    print(str(created_date))
    
    if image_date <= today_date: 
        today_idc = FALSE
    return today_idc
