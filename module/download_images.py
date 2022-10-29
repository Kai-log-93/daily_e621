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
import urllib.request


def download_images():

    # select url in sqlite3
    
    # download time control
    
    # download from url

    
    # define image name

    # Open the response into a new file called <image_name>
    urllib.request.urlretrieve(image_url, image_name)

    return