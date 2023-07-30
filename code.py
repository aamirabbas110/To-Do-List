def display_tasks(tasks):
    print("To-Do List:")
    print("------------")
    for i, task in enumerate(tasks, 1):
        status = " [x]" if tasks[task]["completed"] else " [ ]"
        print(f"{i}. {status} {task}")
    print("------------")

def add_task(tasks, new_task):
    tasks[new_task] = {"completed": False}
    print(f"Task '{new_task}' added to the To-Do List.")

def remove_task(tasks, task_to_remove):
    if task_to_remove in tasks:
        del tasks[task_to_remove]
        print(f"Task '{task_to_remove}' removed from the To-Do List.")
    else:
        print(f"Task '{task_to_remove}' not found in the To-Do List.")

def mark_task_completed(tasks, completed_task):
    if completed_task in tasks:
        tasks[completed_task]["completed"] = True
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print(f"Task '{completed_task}' not found in the To-Do List.")

def main():
    tasks = {}

    while True:
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            task_to_remove = input("Enter the task to remove: ")
            remove_task(tasks, task_to_remove)
        elif choice == "3":
            completed_task = input("Enter the completed task: ")
            mark_task_completed(tasks, completed_task)
        elif choice == "4":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
