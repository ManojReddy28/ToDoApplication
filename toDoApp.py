class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task is added successfully!")

    def display_tasks(self):
        print("\nIncomplete Tasks:\n")
        for index, task in enumerate(self.tasks):
            print(f"Task number: {index + 1}\nTask Description: {task.description}\nDue: {task.due_date}\nPriority: {task.priority}")

        print("\nCompleted Tasks:")
        for index, task in enumerate(self.completed_tasks):
            print(f"Task number: {index + 1}\nTask Description: {task.description}\nDue: {task.due_date}\nPriority: {task.priority}")

    def mark_as_completed(self, task_index):
        
        task = self.tasks.pop(task_index - 1)
        task.completed = True
        self.completed_tasks.append(task)
        print("Marked Successfully!")

    def update_task(self, task_index, description, due_date, priority):
        task = self.tasks[task_index - 1]
        task.description = description
        task.due_date = due_date
        task.priority = priority
        print("updated successfully!")

    def remove_task(self, task_index):
        del self.tasks[task_index - 1]
        print("Removed Successfully!")
    
    def get_task_length(self):
        return len(self.tasks)
    def get_completed_task_length(self):
        return len(self.completed_tasks)

# Sample Usage
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("0. Exit\n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)
        elif choice == 2:
            todo_list.display_tasks()
        elif choice == 3:
            if todo_list.get_task_length() == 0:
                print("No tasks available to mark!")
            else:
                todo_list.display_tasks()
                task_index = int(input("Enter the task number to mark as completed: "))
                if (1<=task_index<=todo_list.get_task_length()):
                    todo_list.mark_as_completed(task_index)
                else:
                    print("Task number is not found!")
        elif choice == 4:
            todo_list.display_tasks()
            if todo_list.get_task_length() == 0:
                print("No tasks available to update!")
            else:
                task_index = int(input("Enter the task number to update: "))
                if (1<=task_index<=todo_list.get_task_length()):
                    description = input("Enter new description: ")
                    due_date = input("Enter new due date: ")
                    priority = input("Enter new priority: ")
                    todo_list.update_task(task_index, description, due_date, priority)
                else:
                    print("Task number not found!")
        elif choice == 5:
            todo_list.display_tasks()
            if todo_list.get_task_length() == 0:
                print("No tasks available to remove!")
            else:
                task_index = int(input("Enter the task number to remove: "))
                if (1<=task_index<=todo_list.get_task_length()):
                    todo_list.remove_task(task_index)
                else:
                    print("Task number not found!")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")
