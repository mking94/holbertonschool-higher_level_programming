#!/usr/bin/python3
""" Python script that print a header attribute from an URL """

import urllib.request as req
import sys

if len(sys.argv) != 2:
    print("Check the argument")
else:
    with req.urlopen(url=sys.argv[1]) as r:
        print(r.getheader("X-Request-Id"))
