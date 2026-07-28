#!/usr/bin/python3
"""Script that displays the X-Request-Id header of a URL's response."""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
