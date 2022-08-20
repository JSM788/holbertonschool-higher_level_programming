#!/usr/bin/python3
"""Write a Python script that takes 2 arguments in order
to solve this challenge"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    r = requests.get(url)
    js = r.json()
    for i in range(10):
        print("{}: {}".format(js[i].get("sha"),
              js[i].get("commit").get("author").get("name")))
