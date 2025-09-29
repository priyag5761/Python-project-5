from todo import ToDoList

# ------------------ INTERACTIVE MENU ------------------
if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. Show All Tasks")
        print("5. Show Pending Tasks")
        print("6. Show Completed Tasks")
        print("7. Show Progress")
        print("8. Exit")
        print("9.Clear all tasks")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.show_all()
            try:
                index = int(input("Enter task number to remove: ")) - 1
                todo.remove_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number!")

        elif choice == "3":
            todo.show_all()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                todo.mark_done(index)
            except ValueError:
                print("⚠️ Please enter a valid number!")

        elif choice == "4":
            todo.show_all()

        elif choice == "5":
            todo.show_pending()

        elif choice == "6":
            todo.show_done()

        elif choice == "7":
            todo.show_progress()

        elif choice == "8":
            print("\n👋 Exiting To-Do List. Goodbye!")
            # break

        elif choice=="9":
            # print()
            todo.clear_all()
        else:
            print("\n⚠️ Invalid choice! Please try again.")
