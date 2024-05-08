#!/usr/bin/python3
"""Module to print a sorted count of keywords"""

import requests


def count_words_in_title(title, word_list, word_dict):
    """Recursively count occurrences of words in the title"""

    if not word_list:
        return
    word = word_list[0]
    count = title.count(word.lower())  # Count occurrences of word
    if count > 0:
        if word in word_dict:
            word_dict[word] += count
        else:
            word_dict[word] = count
    count_words_in_title(title, word_list[1:], word_dict)


def count_words(subreddit, word_list, word_dict=None, after=None):
    """Function to print a sorted list of given keywords"""

    if word_dict is None:
        word_dict = {}

    # Url for the hot posts api, with no limit on it
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    header = {"User-Agent": "Ubuntu/22.0"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            post = posts[0]['data']
            title = post['title'].lower()
            count_words_in_title(title, word_list, word_dict)
            after = post['name']

            return count_words(subreddit, word_list, word_dict, after)
        else:
            sorted_items = sorted(word_dict.items(), lambda x: x[1],
                                  reverse=True)
            sorted_titles = {item[0]: item[1] for item in sorted_items
                             if item[1] > 0}
            print(sorted_titles)
    else:
        return None
