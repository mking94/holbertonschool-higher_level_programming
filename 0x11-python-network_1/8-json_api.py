#!/usr/bin/python3
""" Python script that send request and return valid json"""
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    d = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=d)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
