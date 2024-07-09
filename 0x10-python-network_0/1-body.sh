#!/bin/bash
# Send a GET request to the URL and save the response header and body
curl -sL -w "$1"
