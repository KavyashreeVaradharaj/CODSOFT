class ToDoList:
    def _init_(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = {"task": task, "completed": False}

    def view_tasks(self):
        for task_id, task_info in self.tasks.items():
            status = "Completed" if task_info["completed"] else "Incomplete"
            print(f"{task_id}. {task_info['task']} - {status}")

    def mark_complete(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed.")
        else:
            print("Task not found.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} removed.")
        else:
            print("Task not found.")


todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Complete\n4. Remove Task\n5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.view_tasks()
    elif choice == "3":
        task_id = int(input("Enter the task ID to mark as complete: "))
        todo_list.mark_complete(task_id)
    elif choice == "4":
        task_id = int(input("Enter the task ID to remove: "))
        todo_list.remove_task(task_id)
    elif choice == "5":
        break