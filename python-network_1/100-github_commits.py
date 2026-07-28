#!/usr/bin/python3
"""Script that lists 10 commits (from most recent to oldest) of a repository
by a given owner/user using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name
    )

    response = requests.get(url)
    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except (ValueError, IndexError, AttributeError):
        pass
