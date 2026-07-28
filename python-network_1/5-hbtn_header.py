#!/usr/bin/python3
"""Script that displays the X-Request-Id header of a URL's response."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
