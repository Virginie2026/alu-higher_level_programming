#!/usr/bin/python3
"""Script that sends a POST request with an email and prints the body."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={"email": email})
    print(response.text)
