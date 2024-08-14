#!/usr/bin/python3
"""Documenting module"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "linux:com.example.myredditapp:v1.0 (by /u/YourUsername)"
    }

    params = {"limit": 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    for post in data["data"]["children"]:
        print(post["data"]["title"])
