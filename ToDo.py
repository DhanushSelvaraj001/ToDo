def display_tasks():
    try:
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found.")

def add_task(task):
    with open('todo_list.txt', 'a') as file:
        file.write(task + '\n')
    print(f"Task '{task}' added successfully.")

def remove_task(task_index):
    try:
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if 1 <= task_index <= len(tasks):
            task_to_remove = tasks[task_index - 1].strip()
            with open('todo_list.txt', 'w') as file:
                for task in tasks:
                    if task.strip() != task_to_remove:
                        file.write(task)
            print(f"Task '{task_to_remove}' removed successfully.")
        else:
            print("Invalid task index.")
    except FileNotFoundError:
        print("No tasks found.")

while True:
    print("1. Display tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '3':
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please choose again.")
