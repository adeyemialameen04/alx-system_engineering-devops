#!/usr/bin/python3
"""Documenting Module"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API to get titles of hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "linux:com.example.myredditapp:v1.0 (by /u/YourUsername)"
    }

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None if not hot_list else hot_list

    data = response.json()

    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    after = data["data"]["after"]
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
