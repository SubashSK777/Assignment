# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def addTask():
    # Take user input for the task
    task = input("Please enter a task: ")
    # Append the task to the tasks list as a dictionary with keys 'task' and 'completed'
    tasks.append({"task": task, "completed": False})
    # Print a message confirming the task addition
    print(f"Task '{task}' added to the list.")


# Function to list all tasks
def listTasks():
    # Check if there are any tasks
    if not tasks:
        # If no tasks, print a message
        print("There are no tasks currently.")
    else:
        # If there are tasks, print each task with its index and completion status
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"Task #{index}. {task['task']} - {status}")


# Function to delete a task
def deleteTask():
    # Call listTasks to display all tasks before deletion
    listTasks()
    try:
        # Ask user for the index of the task they want to delete
        taskToDelete = int(input("Enter the # to delete: "))
        # Check if the index is valid
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            # If valid, delete the task at the specified index
            del tasks[taskToDelete]
            # Print a message confirming the deletion
            print(f"Task {taskToDelete} has been removed.")
        else:
            # If index is out of range, print an error message
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        # If user input is not a valid integer, print an error message
        print("Invalid input.")


# Function to mark a task as completed
def markTaskComplete():
    # Call listTasks to display all tasks before marking completion
    listTasks()
    try:
        # Ask user for the index of the task they want to mark as completed
        taskToMark = int(input("Enter the # to mark as completed: "))
        # Check if the index is valid
        if taskToMark >= 0 and taskToMark < len(tasks):
            # If valid, mark the 'completed' status of the task as True
            tasks[taskToMark]["completed"] = True
            # Print a message confirming the task completion
            print(f"Task {taskToMark} marked as completed.")
        else:
            # If index is out of range, print an error message
            print(f"Task #{taskToMark} was not found.")
    except ValueError:
        # If user input is not a valid integer, print an error message
        print("Invalid input.")


# Main function to run the to-do list app
if __name__ == "__main__":
    # Print a welcome message
    print("Welcome to the to do list app :)")
    # Start a loop to allow the user to interact with the app until they choose to quit
    while True:
        # Display the menu options
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Quit")
        # Ask the user for their choice
        choice = input("Enter your choice: ")
        # Check the user's choice and call the corresponding function
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            markTaskComplete()
        elif choice == "4":
            listTasks()
        elif choice == "5":
            # If the user chooses to quit, exit the loop
            break
        else:
            # If the user enters an invalid choice, print an error message
            print("Invalid input. Please try again.")
    # Print a goodbye message when the loop ends
    print("See you soon 👋👋")