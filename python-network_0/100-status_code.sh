#!/bin/bash
# Displays only the status code of a HTTP response without using pipes or redirections
curl -s -o /dev/null -w "%{http_code}" "$1"
