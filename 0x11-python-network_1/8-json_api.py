#!/usr/bin/python3
""" Python script that send request and return valid json"""
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        d = {"q": sys.argv[1]}
    else:
        d = {"q": ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data=d)
    try:
        json = req.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
