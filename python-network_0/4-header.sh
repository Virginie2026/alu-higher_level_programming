#!/bin/bash
# Sends a GET request to a URL with a header variable X-HolbertonSchool-User-Id: 98
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
