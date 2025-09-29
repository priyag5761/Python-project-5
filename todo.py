class Task:
    def __init__(self, description):
        self.description = description
        self.status = "Pending"

    def mark_done(self):
        self.status = "Done"

    def __str__(self):
        return f"{self.description} [{self.status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"\n✅ Task added: {description}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"\n🗑️ Task removed: {removed.description}")
        else:
            print("\n⚠️ Invalid task number!")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print(f"\n✔️ Task marked as done: {self.tasks[index].description}")
        else:
            print("\n⚠️ Invalid task number!")

    def show_pending(self):
        print("\n📌 Pending Tasks:")
        pending = [task for task in self.tasks if task.status == "Pending"]
        if pending:
            for i, task in enumerate(pending, 1):
                print(f"{i}. {task.description}")
        else:
            print("No pending tasks!")

    def show_done(self):
        print("\n🎉 Completed Tasks:")
        done = [task for task in self.tasks if task.status == "Done"]
        if done:
            for i, task in enumerate(done, 1):
                print(f"{i}. {task.description}")
        else:
            print("No completed tasks!")

    def show_all(self):
        print("\n📝 All Tasks:")
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list!")

    def show_progress(self):
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.status == "Done")
        print(f"\n📊 Progress: {done}/{total} tasks completed.")
        
    def clear_all(self):
        self.tasks.clear()
        print("\n All tasks are cleared")


# # ------------------ INTERACTIVE MENU ------------------
# if __name__ == "__main__":
#     todo = ToDoList()

#     while True:
#         print("\n===== TO-DO LIST MENU =====")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. Mark Task as Done")
#         print("4. Show All Tasks")
#         print("5. Show Pending Tasks")
#         print("6. Show Completed Tasks")
#         print("7. Show Progress")
#         print("8. Exit")

#         choice = input("Enter your choice (1-8): ")

#         if choice == "1":
#             desc = input("Enter task description: ")
#             todo.add_task(desc)

#         elif choice == "2":
#             todo.show_all()
#             try:
#                 index = int(input("Enter task number to remove: ")) - 1
#                 todo.remove_task(index)
#             except ValueError:
#                 print("⚠️ Please enter a valid number!")

#         elif choice == "3":
#             todo.show_all()
#             try:
#                 index = int(input("Enter task number to mark as done: ")) - 1
#                 todo.mark_done(index)
#             except ValueError:
#                 print("⚠️ Please enter a valid number!")

#         elif choice == "4":
#             todo.show_all()

#         elif choice == "5":
#             todo.show_pending()

#         elif choice == "6":
#             todo.show_done()

#         elif choice == "7":
#             todo.show_progress()

#         elif choice == "8":
#             print("\n👋 Exiting To-Do List. Goodbye!")
#             break

#         else:
#             print("\n⚠️ Invalid choice! Please try again.")
