#!/usr/bin/python3
"""Module for printing top posts"""

import requests


def top_ten(subreddit):
    """Function to print the title of the first 10 hot posts"""

    # Url for the hot posts api, with a limit on it
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "Ubuntu/22.0"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        if 'data' in data:
            if 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    post_data = post['data']
                    print(post_data['title'])
            else:
                print('None')
        else:
            print('None')
    else:
        print('None')
