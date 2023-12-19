#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Main function to fetch data from the API and write to the CSV file.
    """
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    res = requests.get(f"{URL}users/{argv[1]}")
    res = res.json()
    user_name = res['name']

    res = requests.get(f"{URL}todos")
    all_todos = res.json()
    user_todos = [todo for todo in all_todos if todo['userId'] == int(argv[1])]

    with open(f"{iser_id}.csv", 'w', newline='') as file:
              writer = csv.writer(file, quoting=csv.QUOTE_ALL)
              writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
              for task in user_todos:
                  writer.writerow([user_id, user_name, task["completed"], task["title"0]])
