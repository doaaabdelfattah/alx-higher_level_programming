#!/usr/bin/python3
'''Response header value #0
'''
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(url, data=email)
    print(r.text)
