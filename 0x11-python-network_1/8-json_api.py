#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 1:
        var = ""
    else:
        var = argv[1]
    
    url = "http://0.0.0.0:5000/search_user"
    r = request.post(url, data={"q": var})
    try:
        js = r.json()
        if js == {}:
            print("No results")
        else:
            print("[{}] {}".format(js.get("id"), js.get("name")))
    except ValueError:
        print("Not valid JSON")

