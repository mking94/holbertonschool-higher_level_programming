#!/usr/bin/python3
""" Python script that send request to an URL and print response """

import requests
import sys

if len(sys.argv) != 2:
    print("Check the argument")
else:
    res = requests.get(url=sys.argv[1])
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
