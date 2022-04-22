#!/usr/bin/python3
"""
Python script that takes 2 arguments and ists the 10 most
recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    link = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(link)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
