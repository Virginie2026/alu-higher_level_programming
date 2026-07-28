#!/usr/bin/python3
"""Script that sends a POST request with an email and prints the body."""
from urllib.request import urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({"email": email}).encode("utf-8")

    with urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode("utf-8"))
