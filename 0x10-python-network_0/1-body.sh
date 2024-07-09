#!/bin/bash
# Send a GET request to the URL and save the response header and body
curl -sL "$1" -w "%{http_code}" | grep -q "200$"
