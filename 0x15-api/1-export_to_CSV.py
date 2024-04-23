#!/usr/bin/python3
"""Script to export data to csv format"""

import csv
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
        value = [userId, name, status, title]
        data.append(value)

    filename = f"{userId}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
