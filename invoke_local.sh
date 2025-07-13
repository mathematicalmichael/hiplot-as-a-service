#!/bin/bash

payload=$1
content=${2:-application/x-www-form-urlencoded}

# Ensure the payload file exists
if [[ ! -f "$payload" ]]; then
    echo "File not found: $payload"
    exit 1
fi

# Read the content of the file
data=$(<"$payload")

# URL-encode the data using printf
encoded_data=$(printf '%s' "$data" | jq -sRr @uri)

curl -d "data=$encoded_data" -H "Content-Type: $content" -v http://localhost:1234/h
