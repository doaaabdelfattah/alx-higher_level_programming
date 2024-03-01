#!/usr/bin/python3
'''Python script that fetches URL
'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format((r.text)))
    # print("\t- utf8 content: {}".format((html.decode('utf-8'))))
