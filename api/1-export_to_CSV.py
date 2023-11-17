#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.

Exports data into the CSV format.
"""
import requests
import sys
import csv


def get_employee_progress(employee_id):
    # API endpoint
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct URLs for employee and todo data
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos"

    # Retrieve employee and todo data from the API
    employee_info = requests.get(employee_url).json()
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    # Extract relevant information from employee data
    user_id = employee_info.get("id")
    user_name = employee_info.get("name")

    # Create a CSV file with the user_id as the filename
    csv_filename = f"{user_id}.csv"

    # Open the CSV file for writing
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
  
        # Write the header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task to the CSV file
        for task in todo_list:
            task_completed = str(task["completed"])
            task_title = task["title"]
            csv_writer.writerow([user_id, user_name, task_completed, task_title])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Call the function with the provided employee ID
    employee_id = int(sys.argv[1])
    get_employee_progress(employee_id)
