#!/usr/bin/python3
"""Module '2. Recurse it!'
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if after:
        url = \
            "https://www.reddit.com/r/" \
            "{}/hot.json?limit=100&after={}".format(subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = \
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)"}

    request = requests.get(url, headers=header)

    if request.status_code != 200:
        return None

    if request.status_code == 200:
        data = request.json().get("data").get("children")
        after = request.json().get("data").get("after")

        if data is None:
            return None

        for children in data:
            t = children.get("data").get("title")
            hot_list.append(t)

    if after:
        recurse("{}".format(subreddit), after=after)
    return hot_list
