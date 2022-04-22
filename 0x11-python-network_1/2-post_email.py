#!/usr/bin/python3
""" Python script that send data to URL using post method """

import urllib.request as req
import urllib.parse as p
import sys

if __name__ == "__main__":
    d = p.urlencode({"email": sys.argv[2]}).encode("ascii")

    reqs = req.Request(url=sys.argv[1], method="POST", data=d)
    with req.urlopen(reqs) as res:
        print(res.read().decode("utf-8"))
