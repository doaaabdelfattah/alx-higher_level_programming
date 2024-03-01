#!/usr/bin/python3
'''Response header value #0
'''
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    # Encode the data to bytes
    data = urllib.parse.urlencode(email).encode('utf-8')
    
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        # Decode the response content to a string
        print(the_page.decode('utf-8')) 
