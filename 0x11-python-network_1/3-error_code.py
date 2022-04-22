#!/usr/bin/python3
""" Python script that send request to an URL and print httpcode """

import urllib.request as req
import urllib.parse as p
import sys

if len(sys.argv) != 2:
    print("Check the argument")
else:
    if req.urlopen(sys.argv[1]).getcode() == 200:
        with req.urlopen(sys.argv[1]) as r:
            print(r.read().decode("utf-8"))
    else:
        print("Error code: {}".format(req.urlopen(sys.argv[1]).getcode()))
