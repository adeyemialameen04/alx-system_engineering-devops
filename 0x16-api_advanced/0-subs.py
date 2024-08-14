#!/usr/bin/python3
"""Documenting module"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0-subs:v1.0 (by /u/your_reddit_username)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
