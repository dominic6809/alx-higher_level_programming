#!/usr/bin/python3
"""
script that:
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_content)))
        print("\t- content: {}".format(body_content))
        print("\t- utf8 content: {}".format(body_content.decode('utf-8')))
      
