import argparse
import json

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def update_task(index, new_task):
    tasks = load_tasks()
    try:
        tasks[index] = new_task
        save_tasks(tasks)
        print(f"Updated task {index} to: {new_task}")
    except IndexError:
        print(f"Task {index} not found!")

def delete_task(index):
    tasks = load_tasks()
    try:
        task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {task}")
    except IndexError:
        print(f"Task {index} not found!")

def list_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i}: {task}")
    else:
        print("No tasks found!")

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List Manager")
    parser.add_argument('command', choices=['add', 'update', 'delete', 'list'], help='Command to run')
    parser.add_argument('--task', help="The task to add or update")
    parser.add_argument('--index', type=int, help="The index of the task to update or delete")

    args = parser.parse_args()

    if args.command == 'add' and args.task:
        add_task(args.task)
    elif args.command == 'update' and args.index is not None and args.task:
        update_task(args.index, args.task)
    elif args.command == 'delete' and args.index is not None:
        delete_task(args.index)
    elif args.command == 'list':
        list_tasks()
    else:
        print("Invalid command or missing arguments")

if __name__ == '__main__':
    main()
