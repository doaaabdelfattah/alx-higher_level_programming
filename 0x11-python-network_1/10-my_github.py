#!/usr/bin/python3
''' Search API
'''
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Setup Basic Authentication with the provided username and personal access
    basic = HTTPBasicAuth(username, password)
    # Send a GET request to the GitHub API to retrieve user information
    r = requests.get("https://api.github.com/user", auth=basic)
    # Display the user's id
    user_id = r.json().get('id')
    print(user_id)
