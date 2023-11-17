#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.

Exports data into the CSV format.
"""
import csv
import requests
from sys import argv


def export_tasks_to_csv(user_id):
    """ Export user's tasks to a CSV file """
    # API base URL
    url = 'https://jsonplaceholder.typicode.com'

    # URLs for user's todos and user details
    todo_url = f"{url}/users/{user_id}/todos"
    employee_url = f"{url}/users/{user_id}"

    # Get responses from the API
    users_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    # Parse JSON responses
    todo_data = todo_response.json()
    employee_data = users_response.json()

    # Extract user details
    name = employee_data.get("username")

    # Create a dictionary of tasks and their completion status
    tasks = {task["title"]: task['completed'] for task in todo_data}

    # Write data to CSV file
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write header row
        file_writer.writerow(['User ID', 'Name', 'Task Status', 'Task'])

        # Write data rows
        for task, done_status in tasks.items():
            file_writer.writerow([user_id, name, done_status, task])


if __name__ == "__main__":
    # Get user ID from command line arguments
    user_id = int(argv[1])

    # Call the export_to_csv function with the provided user ID
    export_tasks_to_csv(user_id)
