#!/usr/bin/python3
''' Search API
'''
import requests
import sys


if __name__ == "__main__":
    # Extract repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the URL for the GitHub API endpoint to list commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    # Send a GET request to the GitHub API to retrieve user information
    r = requests.get(url)
    # Parse the JSON response
    commits = r.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
