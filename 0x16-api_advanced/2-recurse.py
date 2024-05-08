#!/usr/bin/python3
"""Module to recursively call the reddit api"""

import requests


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """Function to return a list containing the titles of all hot articles
    for a given subreddit """

    # Url for the hot posts api, with no limit on it
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "Ubuntu/22.0"}
    if after:
        url += "?after={}".format(after)

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            add_title(hot_list, posts)
            after = data['data']['after']

            if not after:
                return hot_list
            return recurse(subreddit, hot_list, after)
        else:
            return None
    else:
        return None
