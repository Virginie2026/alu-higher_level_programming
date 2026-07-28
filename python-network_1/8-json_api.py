#!/usr/bin/python3
"""Script that searches for a user by letter via a POST request."""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        json_body = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not json_body:
            print("No result")
        else:
            for user in json_body:
                print("[{}] {}".format(user.get("id"), user.get("name")))
