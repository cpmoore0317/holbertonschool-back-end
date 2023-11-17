#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


def get_completed_tasks(user_id):
    """Returns a list of completed tasks for a given user ID."""
    base_api_url = 'https://jsonplaceholder.typicode.com'
    url = f'{base_api_url}/users/{user_id}/todos?_expand=user'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return None

    todo_data = json.loads(response.text)
    completed_tasks = [task for task in todo_data if task['completed']]
    return completed_tasks

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: get_completed_tasks.py <user_id>")
        exit(1)

    user_id = argv[1]
    completed_tasks = get_completed_tasks(user_id)

    if completed_tasks is None:
        exit(1)

    employee_name = completed_tasks[0]['user']['name']
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    first_line = (
        f"Employee {employee_name} is done with tasks"
        f"({num_completed_tasks}/{total_tasks}):")
    print(first_line)

    for task in completed_tasks:
        print(f"\t {task['title']}")
