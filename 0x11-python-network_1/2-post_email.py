#!/usr/bin/python3
""" Python script that send data to URL using post method """

import urllib.request as req
import urllib.parse as p
import sys

if len(sys.argv) != 3:
    print("Check the argument")
else:
    d = p.urlencode({"email": sys.argv[2]}).encode("ascii")
    rq = req.Request(sys.argv[1], d)
    with request.urlopen(rq) as res:
        print(res.read().decode("utf-8"))
