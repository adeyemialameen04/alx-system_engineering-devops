#!/usr/bin/python3
"""Documenting module"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers in subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Agent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
