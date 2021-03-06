#!/usr/bin/python3
""" Python script that fetche an URL """

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
    html = res.read()
print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.decode("utf-8")))
