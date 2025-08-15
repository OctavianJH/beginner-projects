#Subprograms

def viewTasks():
    print("View all tasks:")

def addTasks():
    print("Add a new task:")
    
def deleteTasks():
    print("Delete a task:")

def main():
    print("Welcome to the To-Do List application!")
    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ")
        
        if choice == '1':
            viewTasks()
        elif choice == '2':
            addTasks()
        elif choice == '3':
            deleteTasks()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def loadFile(filename):
    try:
        with open(filename, "r") as f:
            tasks = [line.strip()for line in f]
            
    except FileNotFoundError as e:
        print(f"Sorry, there was an error: {e}")
        tasks = []
        
        return tasks
            
            
        
    


#Main

main()