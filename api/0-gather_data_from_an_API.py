#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Replace 'API_URL' with the actual API URL
    api_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + str(employee_id)

    response = requests.get(api_url)
    if response.status_code == 200:
        todo_list = response.json()

        completed_tasks = list(filter(lambda task: task['completed'], todo_list))
        total_tasks = len(todo_list)
        done_tasks_count = len(completed_tasks)

        print(f"Employee {completed_tasks[0]['user']['name']} is done with tasks({done_tasks_count}/{total_tasks}):")

        for task in completed_tasks:
            task_title = task['title']
            print(f"\t {task_title}")

    else:
        print(f"Error fetching employee TODO list progress: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)