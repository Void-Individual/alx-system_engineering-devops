#!/usr/bin/python3
"""Function to return the num of subscribers in a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function to return the no of subscribers"""

    count = 0
    # Reddit API for getting subreddit info
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # A custom header to avoid being denied access by reddit
    header = {"User-Agent": "Mozilla/5.0"}

    # Send a get request to the reddit API
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        # If the response is successful with status code 200
        data = response.json()
        if 'data' in data:
            if 'subscribers' in data['data']:
                count = data['data']['subscribers']

    return count
