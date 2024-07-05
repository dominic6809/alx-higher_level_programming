#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
using requests
"""

if __name__ == "__main__":
    import requests
    
    url = "https://alx-intranet.hbtn.io/status"
    
    res = requests.get(url)
    body_content = res.text
    
    print("Body response:")
    print("\t- type: {}".format(type(body_content)))
    print("\t- content: {}".format(body_content))
    print("\t- utf8 content: {}".format(body_content))
