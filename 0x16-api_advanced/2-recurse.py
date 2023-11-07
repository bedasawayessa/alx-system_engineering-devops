#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
from requests import get


def recurse(subreddit, hot_list=[], next=""):
    """
    Hot posts by subreddit in a recursive way
    """
    headers = {"user-agent": "kyeeh"}
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, next)
    try:
        req_data = get(url, headers=headers, allow_redirects=False).json()
        hot_posts = req_data["data"]["children"]
        for post in hot_posts:
            hot_list.append(post['data']['title'])
        next = req_data['data']['after']
        if next:
            recurse(subreddit, hot_list, next)
        return (hot_list)
    except Exception:
        return (None)
