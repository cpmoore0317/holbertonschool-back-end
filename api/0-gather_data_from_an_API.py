#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import json
from sys import argv
import requests

if __name__ == '__main__':
    # Base URL for the JSONPlaceholder API
    base_api_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve user ID from command-line arguments
    target_user_id = argv[1]

    # Make a request to the API to fetch the to-do list for the specified user
    response = requests.get(f'{base_api_url}/users/{target_user_id}/todos?_expand=user')

    if response.status_code == 200:
        # Load JSON data from the response
        todo_data = response.json()

        # Extract employee name from the first task
        employee_name = todo_data[0]['user']['name']

        # Filter completed tasks
        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        # Display the summary
        first_line = f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):"
        print(first_line)

        for task in completed_tasks:
            print(f"\t {task['title']}")
    else:
        print(f"Error: {response.status_code}")