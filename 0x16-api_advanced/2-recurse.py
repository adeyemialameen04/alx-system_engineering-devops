#!/usr/bin/python3
"""Module to query Reddit API and get titles of hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API to get titles of hot articles
    """
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Headers to avoid Too Many Requests error
    headers = {
        "User-Agent": "linux:com.example.myredditapp:v1.0 (by /u/YourUsername)"
    }

    # Parameters for the API request
    params = {"limit": 100}  # Maximum allowed by Reddit API
    if after:
        params["after"] = after

    # Make the API request
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return None if not hot_list else hot_list

    # Parse the response
    data = response.json()

    # Extract post titles and add to hot_list
    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    # Check if there are more pages
    after = data["data"]["after"]
    if after:
        # Recursive call with the new 'after' value
        return recurse(subreddit, hot_list, after)
    else:
        # Base case: no more pages, return the complete list
        return hot_list
