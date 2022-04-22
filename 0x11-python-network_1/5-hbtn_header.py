#!/usr/bin/python3
""" Python script that send request to an URL and print specific header """

import requests
import sys

if len(sys.argv) != 2:
    print("Check the argument")
else:
    res = requests.get(url=sys.argv[1])
    print(res.headers['X-Request-Id'])
