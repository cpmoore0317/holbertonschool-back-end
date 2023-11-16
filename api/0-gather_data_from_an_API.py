#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


import json
import urllib.request
from sys import argv

def get_todo_data(user_id):
    api_url = 'https://jsonplaceholder.typicode.com'
    url = f'{api_url}/users/{user_id}/todos?_expand=user'

    with urllib.request.urlopen(url) as response:
        if response.getcode() == 200:
            return json.loads(response.read())
        else:
            print(f"Error: {response.getcode()}")
            return None

def main():
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        return

    user_id = argv[1]
    todo_data = get_todo_data(user_id)

    if todo_data:
        employee_name = todo_data[0]['user']['name']
        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

if __name__ == '__main__':
    main()
