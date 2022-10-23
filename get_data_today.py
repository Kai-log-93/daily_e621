# using the requests library to access internet data

from operator import truediv
from pickle import TRUE
import sys
import requests
from requests.exceptions import HTTPError, Timeout
import json
import sqlite3
from sqlite3.dbapi2 import Cursor
from module.load_to_sqlite import load_to_sqlite
from filters.filter_date import filter_date

def main():
    # Use requests to issue a standard HTTP GET request
    try:
        # List: The base URL is /posts.json called with GET.
        # dataValues = { 'tags' : 'bomb_(artist)', 'limit': '50'}
        dataValues = { 'tags' : 'muscular_male horse bull', 'limit': '200'}
        headerValues = { 'User-Agent' : 'Daily Fur App / 1.0 (by GypsyMonkey on e621)' }
        url = "https://e621.net/posts.json"
        # url = "http://httpbin.org/delay/5"
        # result = requests.get(url, params=dataValues, timeout=5)
        result = requests.get(url, params=dataValues, headers=headerValues)
        # raise_for_status will throw an exception if an HTTP error
        # code was returned as part of the response
        result.raise_for_status()

        # Use the built-in JSON function to return parsed data
        dataobj = result.json()
        # print(json.dumps(dataobj,indent=4)) # 缩进4
        # Access data in the python object
        print(list(dataobj.keys()))

        # 因为数据结构的原因, 所有数据放在 [] 中, 第二位只能用数字做下标
        print('--------------------------------')
        images_key_info = []
        today_idc = TRUE
        for images in dataobj['posts']: 
            image_datetime = str(images['created_at'])
            # if not today image, then pass it  
            if filter_date(image_datetime, today_idc):
                pass
            images_key_info.append((images['file']['width'], 
                                    images['file']['height'], 
                                    images['file']['ext'], 
                                    images['file']['url'],
                                    images['created_at']))
                                  
        # load all image download to the sqlite db    
        load_to_sqlite(images_key_info)

    # if http error
    except HTTPError as err:
        print("Error: {0}".format(err))
    # if time out
    except Timeout as err:
        print("Request timed out: {0}".format(err))
        
if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    main()
