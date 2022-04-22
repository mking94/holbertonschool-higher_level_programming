#!/usr/bin/python3
""" Python script that send data to URL using post method """

import urllib.request as req
import urllib.parse as p
import sys

if len(sys.argv) != 3:
    print("Check the argument")
else:
    d = p.urlencode({"email": sys.argv[2]})
    d = d.encode("ascii")
    r = req.Request(url=sys.argv[1], method="POST")
    r = request.urlopen(r, d)
    with r.read() as res:
        print(res.decode("utf-8"))
