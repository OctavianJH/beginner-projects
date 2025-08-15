#Lists
tasks = []

#Subprograms
def viewTasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def save_tasks(filename, tasks):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def deleteTasks(filename):
    global tasks
    if not tasks:
        print("No tasks to delete!")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
            save_tasks(filename, tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def displayMenu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Quit")


def main():
    global tasks
    filename = "tasks.txt"
    tasks = loadTasks(filename)

    while True:
        displayMenu()
        choice = input("Choose an option between 1-4: ")

        if choice == '1':
            viewTasks()

        elif choice == '2':
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added.")
            save_tasks(filename, tasks)

        elif choice == '3':
            deleteTasks(filename)

        elif choice == "4":
            save_tasks(filename, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


def loadTasks(filename):
    try:
        with open(filename, "r") as f:
            tasks = [line.strip() for line in f]
    except FileNotFoundError:
        print("No existing task file found. Starting fresh.")
        tasks = []
    return tasks


#Main
main()