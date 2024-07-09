#!/bin/bash
# bash script that Sends a DELETE request to a given URL and display the response body.
echo ""; curl -s -X DELETE "$1"
