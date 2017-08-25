# Google Trends Unofficial API 
# 8/24/2017
# Data Mining Tool
# Xavier Collantes

import requests
import json
from pytrends.request import *

def main():
    google_username = 'collx24@gmail.com'
    google_password = 'Hello123'
    query_list = ['lipstick'] # Can include up to 5 terms. 

    time_zone = 360
    hl = 'en-US'

    country_abbv = '' # Defaults to World. ex. ('US' 'US-WA' 'GB-ENG' 'PH' 'HK')
    
    output_file_path()
    pytrends = TrendReq(google_username, google_password, hl, time_zone, custom_useragent=None)
    #print (type(pytrends))
    pytrends.build_payload(query_list, cat=0, timeframe='today 5-y', country_abbv, gprop='')



    print (pytrends.interest_over_time())


def output_file_path(path):
    output(path)
    
# File output file
def output(data):
    f = open("./data_output.csv", "w+")
    print("Opening file: " + f.name)

    
    f.write(str(data))
    print("Written to: " + f.name)
    f.close()
    print(f.name + " closed.")

main()
