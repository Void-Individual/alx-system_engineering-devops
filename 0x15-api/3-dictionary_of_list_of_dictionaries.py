#!/usr/bin/python3
"""Script to export all the API data to JSON"""

import json
import requests

if __name__ == "__main__":

    url = f"https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    dump = {}
    for user in users:
        name = user.get("username")
        userId = user.get("id")

        url = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
        all_tasks = requests.get(url).json()
        data = []
        for task in all_tasks:
            status = task.get("completed")
            title = task.get("title")
            value = {"task": title, "completed": status, "username": name}
            data.append(value)
        dump[userId] = data

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(dump, file)
