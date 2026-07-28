#!/usr/bin/python3
"""Script that fetches a URL and handles HTTP errors gracefully."""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
