#!/usr/bin/python3
""" Python script that send data to URL and print the response """

import requests
import sys

if len(sys.argv) != 2:
    print("Check the argument")
else:
    d = {"email": sys.argv[2]}
    res = requests.post(url=sys.argv[1], data=d)
    print(res.text)
