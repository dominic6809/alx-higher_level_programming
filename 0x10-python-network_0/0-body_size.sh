#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response.

# Make sure a URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Fetch the Content-Length from the headers
size=$(curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2)

# If Content-Length is not found, download the body and measure the size
if [ -z "$size" ]; then
  size=$(curl -s "$1" | wc -c)
fi

# Display the size in bytes
echo "$size"
