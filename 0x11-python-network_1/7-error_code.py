#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response.
If the HTTP status code is >= 400,
prints: Error code: followed by the HTTP status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
