import json
import os

def load_task( filename="task.json"):
    if os.path.exists(filename):
     with open(filename, "r") as file:
        tasks = json.load(file)
    else :
        tasks = {}
    return tasks

def save_task(tasks, filename="task.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)    

def add_task(tasks):
    task_description = input("Enter the task description: ")
    task_priority = input("Enter the task priority(High, Medium, Low): ")
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": task_description,
        "completed": False,
        "priority": task_priority
    }
    tasks.append(task)
    print(f"Task with ID:{task_id} has added succesfully!")

def view_task(tasks):
    if not tasks :
        print("No tasks available!")
    else :
        for task in tasks :
            status = 'completed' if task['completed'] else 'not completed'
            print(f"ID: {task['id']}, Task: {task['description']}, Status: {status}, Priority: {task['priority']}")

def mark_task_completed(tasks):
    task_id = int(input("Enter the task ID: "))
    for task in tasks :
        if task['id'] == task_id :
            task['completed'] = True
            print(f"Task with ID:{task_id} has marked completed")  
        else:
            print(f"No task available with ID:{task_id}")                  

def delete_task(tasks):
    task_id = int(input("Enter the task ID: "))
    for task in tasks :
        if task['id'] == task_id:
            tasks.remove(task)
            print(f'Task with ID:{task_id} was deleted succesfully!')
        else:
            print(f"No task available with ID:{task_id}")

def sort_task(tasks):
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda task: priority_order[task['priority']])
    print("Tasks sorted by priority!")

def edit_task(tasks):
    task_id = int(input("Enter the task ID to edit: "))
    new_description = input("Enter the new task: ")
    new_priority = input("Enter the new priority(High, Medium, Low): ")
    for task in tasks :
        if task['id'] == task_id:
            task['description'] = new_description
            task['priority'] = new_priority
            print(f"Task with ID:{task_id} has edited succesfully!")
def main():
    task = []
    while True:
        print("\nMenu")
        print("1. Add task")            
        print("2. View task")            
        print("3. Mark task")     
        print("4. Delete task")
        print("5. Sort task")
        print("6. Edit task")
        print("5. Save and Quit")
        choice = int(input("Enter your choice: ")) 

        if choice == 1:
            add_task(task)
        elif choice == 2:
            view_task(task)
        elif choice == 3:
            mark_task_completed(task)
        elif choice == 4:
            delete_task(task)
        elif choice == 5:
            sort_task(task)
        elif choice == 6:
            edit_task(task)
        elif choice == 7:        
            print("Saved and Exiting the program!")
            break
        else: 
            print("Invalid choice. Please try again...")                      

if __name__ == "__main__" :
    main()           