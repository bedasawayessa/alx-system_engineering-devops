#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    data = response.json()
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()['name']
    total_tasks = len(data)
    done_tasks = sum(task['completed'] for task in data)
    print("Employee {} is done with tasks({}/{}):".format(user_name, done_tasks, total_tasks))
    for task in data:
        if task['completed']:
            print("\t {}".format(task['title']))
