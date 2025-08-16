import sys
import os



#Show Menu subprogram.
def viewTasks(filename):
    try: 
    
        if not os.path.exists(filename):
            print("No tasks yet.")
            return
    
        with open(filename, "r") as f:
            for task in f:
                print(task.strip())
    


            
    except ValueError:
        print("Error. Please try again.")
    

def addTasks(filename):
    try:
        userTask = input("Please enter the task you want added: ")
        
        if not userTask:
            print("Task cannot be empty.")
            return
        
        with open(filename, "a") as f:
            f.write(userTask + "\n")
            
        with open(filename, "r") as f:
            print("Your new tasks list is:")
            for line in f:
                print(line.strip())

                    
    except ValueError as e:
        print(f"Please try again, there was an error: {e}")        


def deleteTasks(filename):
    
    if not os.path.exists(filename):
        print("No tasks to delete.")
        return

    with open(filename, "r") as f:
        tasks = f.readlines()
        
    if not tasks:
        print("No tasks to delete.")
        return

        
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")
    
    try:
        userInput = int(input("Please enter the corresponding digit of the task you want to delete: "))
        
        if 1 <= userInput <= len(tasks):
            tasks.pop(userInput - 1)
            
            with open(filename, "w") as f:
                f.writelines(tasks)
            
            print("Task deleted. Your new tasks list is:")
            for task in tasks:
                print(task.strip())
        else:
            print("Invalid task number.")
    
    except ValueError as e:
        print(f"Please try again, there was an issue: {e}")    
            

def quitApp():
    sys.exit()


def showMenu():
    print("\n 1. View Tasks ")
    print("\n 2. Add Tasks ")
    print("\n 3. Delete Tasks ")
    print("\n 4. Quit ")

def userChoice(filename):
    try:
        userInput = int(input("Please enter the corresponding number: "))
        if userInput == 1:
            viewTasks(filename)
            
            return userInput
        
        elif userInput == 2:
            addTasks(filename)

            return userInput
        
        elif userInput == 3:
            deleteTasks(filename)
            
            return userInput
        
        else:
            quitApp()
            
            return userInput
    
    except ValueError as e:
        print(f"Please try again, there was an error {e}")
        

def main(filename):
    while True: 
        showMenu()
        userChoice(filename)

#Main

filename = "tasks.txt"

main(filename)