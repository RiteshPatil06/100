#making a list of task
Task = []

#function to add task
def add_task(tasks):
    task_description = input("Enter the task description: ")
    task_id = len(tasks) + 1 #generate unique id for each task
    task = {
        "id": task_id,
        "description": task_description,
        "completed": False
    }
    tasks.append(task)
    print(f"Task added with ID: {task_id}")

#function to view task
def view_task(tasks):
              if not tasks:
               print("No tasks available")    
              else :
                    for task in tasks:
                          status = "completed" if task['completed'] else "not completed"
                          print(f"ID: {task['id']}, Task: {task['description']}, Status: {status}")

#function to delete task
def delete_task(tasks):
      task_id = int(input("Enter the task ID to delete: ")) 
      for task in tasks:
            if task['id'] == task_id :
             tasks.remove(task)
             print(f"Task with ID:{task_id} removed succesfully!")
             return
      print(f"No such task were found with ID: {task_id}")

#function to mark task
def mark_task_completed(tasks):
      task_id = int(input("Enter the task ID to mark as completed"))
      for task in tasks:
            if task['id'] == task_id :
              task['completed'] = True
              print(f"Task with ID: {task_id} marked as completed.")
              return
            print(f"No such task were found with ID: {task_id}.")
                                  
def main():
     tasks = []
     while True:
          print("\nMenu:") #menu for user interaction
          print("1. Add Task")
          print("2. View Tasks")
          print("3. Delete Task")
          print("4. Mark Task as Completed")
          print("5. Quit")
          choice = int(input("Enter your choice: "))
          
          if choice == 1:
               add_task(tasks)
          elif choice == 2:
               view_task(tasks)
          elif choice == 3:
               delete_task(tasks)
          elif choice == 4:
               mark_task_completed(tasks)
          elif choice == 5:
               print("Exiting the program.")
               break
          else: 
               print("Invalid choice.please try again...")

if __name__ == "__main__":
     main()                         

