#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    res = requests.get(url, auth=(username, token))
    
    try:
        json_response = res.json()
        print(json_response.get("id"))
    except ValueError:
        print("Not a valid JSON")
