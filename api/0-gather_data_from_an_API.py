#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def first_line(id):
    """ Fetch user name """

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']

    filename = 'student_output'

    with open(filename, 'r') as f:
        first = f.readline().strip()

    if name and name.strip() in first:
        print("Employee Name: OK")
    else:
        print("Employee Name: Incorrect")


def get_employee_todo_progress(employee_id):
    # API URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user name
    user_resp = requests.get(users_url).json()
    employee_name = next((user['name'] for user in user_resp if user['id'] == employee_id), None)

    if not employee_name:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    # Fetch tasks information
    todos_resp = requests.get(todos_url).json()
    total_tasks = len([todo for todo in todos_resp if todo['userId'] == employee_id])
    completed_tasks = len([todo for todo in todos_resp if todo['userId'] == employee_id and todo['completed']])

    # Display information
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_resp:
        if todo['userId'] == employee_id and todo['completed']:
            print(f"    {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
