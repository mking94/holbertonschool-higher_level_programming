#!/usr/bin/python3
""" Python script that send data to URL and print the response """

import requests
import sys

if __name__ == '__main__':
    d = {"email": sys.argv[2]}
    res = requests.post(url=sys.argv[1], data=d)
    print(res.text)
