#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import json


def get_employee_progress(employee_id):
    """
    Retrieve and display the progress of an employee's completed tasks.

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
    employee_name = employee_info.get("username")

    # Filter completed tasks from the todo list
    completed_tasks = [
        {"username": employee_name, "task": task["title"], "completed": task["completed"]}
        for task in todo_list
    ]

    return completed_tasks


def export_all_employees():
    """
    Export data in JSON format for all employees and save it to a file.
    """
    # Number of employees (you may change it based on your actual data)
    num_employees = 10

    # Create a dictionary to store data for all employees
    all_employees_data = {}

    # Loop through all employee IDs
    for employee_id in range(1, num_employees + 1):
        employee_data = get_employee_progress(employee_id)
        all_employees_data[str(employee_id)] = employee_data

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file)


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Call the function with the provided employee ID
    employee_id = int(sys.argv[1])
    employee_progress = get_employee_progress(employee_id)

    # Display the employee's task progress
    print(f"Employee {employee_progress[0]['username']} is done with tasks:")
    for task in employee_progress:
        print(f"\t {task['task']}")

    # Export data for all employees
    export_all_employees()
