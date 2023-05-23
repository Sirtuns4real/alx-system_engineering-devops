#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve user information
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    user = user_response.json()

    # Retrieve todos for the user
    todos_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos if task["completed"]]

    return user, completed_tasks

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID.")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    user, completed_tasks = get_employee_todo_list(employee_id)
    
    print("Employee {} is done with tasks ({}/{}):".format(
        user["name"], len(completed_tasks), len(todos)))
    
    for task in completed_tasks:
        print("\t{}".format(task))
