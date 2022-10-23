from pickle import FALSE, TRUE
import sys
import json
import time
import datetime
from datetime import date

def filter_date(image_datetime, today_idc):
    # get todays' date
    today_date = date.today().strftime("%Y/%m/%d")
    # today_date = time.strptime(today_date, "%d/%m/%Y")
    print(str(today_date))
    image_date = str(image_datetime[0:10])
    # created_date is the image uploaded date
    created_date = datetime.datetime.strptime(image_date, '%Y-%m-%d').strftime("%Y/%m/%d")
    print(str(created_date))
    
    # 比对时间， 今天之前的数据全部筛掉
    # 只有dd/mm/yy 格式的日期可以进行比对
    if image_date <= today_date: 
        today_idc = FALSE
    
    # return the indicator 
    return today_idc
