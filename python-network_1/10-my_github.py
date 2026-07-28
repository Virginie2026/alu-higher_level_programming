#!/usr/bin/python3
"""Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id using HTTP Basic Authentication.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))
    try:
        user_data = response.json()
        print(user_data.get("id"))
    except ValueError:
        print("None")
