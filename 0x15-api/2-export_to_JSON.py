#!/usr/bin/python3
"""Script to export API data to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{userId}"
    user_info = requests.get(url).json()
    name = user_info.get("username")

    url = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    all_tasks = requests.get(url).json()
    data = []
    for task in all_tasks:
        status = task.get("completed")
        title = task.get("title")
        value = {"task": title, "completed": status, "username": name}
        data.append(value)
    user = {userId: data}

    filename = f"{userId}.json"
    with open(filename, mode='w') as file:
        json.dump(user, file)
