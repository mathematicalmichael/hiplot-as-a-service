#!/bin/bash

payload=$1
content=${2:-multipart/form-data}

curl -F data=@${payload} -H "Content-Type: ${content}" -v http://localhost:8081/h
