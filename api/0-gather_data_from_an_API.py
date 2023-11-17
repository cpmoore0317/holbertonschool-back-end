#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


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
    employee_name = employee_info.get("name")

    # Filter completed tasks from the todo list
    completed_tasks = [task["title"] for task in todo_list if task["completed"]]

    # Calculate the number of completed and total tasks
    number_completed = len(completed_tasks)
    number_total = len(todo_list)

    # Display the employee's task progress
    print(f"Employee {employee_name} is done with tasks({number_completed}/{number_total}):")

    # Display each completed task
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Call the function with the provided employee ID
    employee_id = int(sys.argv[1])
    get_employee_progress(employee_id)
