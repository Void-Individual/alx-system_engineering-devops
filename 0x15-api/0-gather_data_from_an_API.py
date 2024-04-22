#!/usr/bin/python3
"""Python script to return information from an API"""

import sys
import requests

if __name__ == "__main__":

    userId = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{userId}"
    response = requests.get(url)
    user_info = response.json()
    name = user_info.get("name")

    url = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    response = requests.get(url)
    all_tasks = response.json()

    done = 0
    undone = 0
    total = 0
    titles = []
    for task in all_tasks:
        if task.get("completed") is True:
            done += 1
            titles.append(task.get("title"))
        else:
            undone += 1
        total += 1
    print(f"Employee {name} is done with tasks({done}/{total})")
    for title in titles:
        print(f"\t {title}")
