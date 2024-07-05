#!/usr/bin/python3
"""
Takes repository name and owner name as arguments
and lists 10 most recent commits from the repository.
Prints commits in the format: <sha>: <author name>
(line 20)This will raise an HTTPError for bad responses (4xx or 5xx)
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{}/{}/commits"

    try:
        res = requests.get(url)
        res.raise_for_status()
        commits = res.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except (KeyError, TypeError, ValueError) as e:
        print(f"Error processing JSON response: {e}")
