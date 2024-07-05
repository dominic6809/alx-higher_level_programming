#!/bin/bash
# Send a GET request to the URL and save the response header and body
curl -sL -w "%{http_code}" "$1" -o ./output -D ./header

# Check if the HTTP status code is 200 OK
if grep -q "200 OK" ./header; then
    # Display the body of the response
    cat ./output
fi
