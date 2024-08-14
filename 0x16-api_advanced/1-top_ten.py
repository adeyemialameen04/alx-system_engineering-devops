#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Headers to avoid Too Many Requests error
    headers = {
        "User-Agent": "linux:com.example.myredditapp:v1.0 (by /u/YourUsername)"
    }

    # Parameters for the API request
    params = {"limit": 10}  # Limit to 10 posts

    # Make the API request
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    # Parse the response
    data = response.json()

    # Print the titles of the first 10 hot posts
    for post in data["data"]["children"]:
        print(post["data"]["title"])
