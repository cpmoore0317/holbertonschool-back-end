#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.

Exports data in the JSON format.
"""
import json
import requests
import sys


def export_progress_to_json(employee_id):
    """
    Retreive and display the progress of an employee's completed tasks.

    Args:
    - employee_id (int): The ID of the employee.
    """
    # API endpoint
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct URLs for employee and todo data
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos"

    # Retrieve employee and todo data from the API
    employee_info = requests.get(employee_url).json()
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    # Extract relevant information from employee data
    employee_name = employee_info.get("name")

    # Filter completed tasks from the todo list
    completed_tasks = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_info["username"],
        }
        for task in todo_list
    ]

    # Create a dictionary with the employee ID as the key and the completed
    employee_data = {str(employee_id): completed_tasks}

    # Save the data to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(employee_data, json_file, indent=2)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Call the function with the provided employee ID
    employee_id = int(sys.argv[1])
    export_progress_to_json(employee_id)
