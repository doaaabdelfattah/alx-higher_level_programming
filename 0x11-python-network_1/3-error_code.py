#!/usr/bin/python3
''' Error code #0
'''
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
