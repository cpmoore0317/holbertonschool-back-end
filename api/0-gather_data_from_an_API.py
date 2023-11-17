#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import requests


def get_employee_progress(employee_id):
    """ Display the employee's todo list progress """
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/todos"

    user_data = requests.get(user_endpoint).json()
    todo_data = requests.get(todo_endpoint,
                             params={"userId": employee_id}).json()

    employee_name = user_data.get("name")
    completed_tasks = [task["title"] for task in todo_data 
                       if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} has completed 
          {num_completed_tasks}/{total_tasks} tasks:")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_progress(employee_id)
