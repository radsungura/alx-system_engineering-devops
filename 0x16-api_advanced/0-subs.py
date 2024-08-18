#!/usr/bin/python3
"""Function to return the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux"
    }
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code == 404:
        return 0
    return result.json().get("subscribers").get("data")
