#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

curl -s -d @"$2" -H "Content-Type: application/json" "$1" -X POST
