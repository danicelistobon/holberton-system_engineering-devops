#!/usr/bin/python3
"""Module '1. Top Ten'
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts
        listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    request = requests.get(url, headers=header)

    if request.status_code == 200:
        data = request.json().get("data").get("children")
        for children in data:
            title = children.get("data").get("title")
            print(title)
    else:
        print('None')
