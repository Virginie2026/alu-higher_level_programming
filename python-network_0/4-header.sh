#!/bin/bash
# Sends a GET request to a URL with a specific header variable
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
