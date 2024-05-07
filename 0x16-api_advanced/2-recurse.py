#!/usr/bin/python3
"""Module to recursively call the reddit api"""

import requests


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
            if len(posts) == 0:
                return hot_list

            post = posts[0]
            post_data = post['data']
            title = post_data['title']
            after = post_data['name']
            hot_list.append(title)
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return hot_list
