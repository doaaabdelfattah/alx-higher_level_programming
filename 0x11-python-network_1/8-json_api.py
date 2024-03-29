#!/usr/bin/python3
''' Search API
'''
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    payload = {'q': letter}
    r = requests.post(url, data=payload)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
