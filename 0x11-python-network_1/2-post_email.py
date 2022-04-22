#!/usr/bin/python3
""" Python script that send data to URL using post method """

import urllib.request as req
import urllib.parse as p
import sys

d = p.urlencode({"email": sys.argv[2]})
d = d.encode("ascii")
r = req.Request(url=sys.argv[1], d)
r = request.urlopen(req)
with r.read() as res:
    print(res.decode("utf-8"))
