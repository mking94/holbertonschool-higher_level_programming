#!/usr/bin/python3
""" Python script that send request to an URL and print httpcode """

import urllib.request as req
import urllib.error as err
import sys

if len(sys.argv) != 2:
    print("Check the argument")
else:
    try:
        with req.urlopen(sys.argv[1]) as r:
            print(r.read().decode("utf-8"))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
