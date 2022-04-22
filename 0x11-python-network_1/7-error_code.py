#!/usr/bin/python3
""" Python script that send data to URL and print the response code """

import requests
import sys

if __name__ == '__main__':
    res = requests.get(url=sys.argv[1])
    if res.status_code == 200:
        print(res.text)
    else if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
