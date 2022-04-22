#!/usr/bin/python3
""" Python script that send request to an URL and print response """

import requests
import sys

res = requests.get(url="https://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(res.text)))
print("\t- content: {}".format(res.text))
