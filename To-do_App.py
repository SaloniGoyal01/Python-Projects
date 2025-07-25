def task():
    tasks = []  # Initialize an empty list to store tasks
    print("Welcome to the Task Management App")

    # Add initial tasks
    try:
        total_task = int(input("Enter how many tasks you want to add: "))
        for i in range(1, total_task + 1):
            task_name = input(f"Enter task {i}: ")
            tasks.append(task_name)
    except ValueError:
        print("Invalid input! Number expected.")
        return  # Exit if invalid input at the beginning

    print(f"Today's tasks are:\n{tasks}")

    # Start operations loop
    while True:
        try:
            operation = int(input(
                "\nEnter your choice:\n"
                "1 - Add\n"
                "2 - Update\n"
                "3 - Delete\n"
                "4 - View\n"
                "5 - Exit/Stop\n"
                "Choice: "
            ))

            if operation == 1:
                add = input("Enter task you want to add: ")
                tasks.append(add)
                print(f"✅ Task '{add}' has been successfully added.")

            elif operation == 2:
                update = input("Enter the task name you want to update: ")
                if update in tasks:
                    up = input("Enter new task: ")
                    ind = tasks.index(update)
                    tasks[ind] = up
                    print(f"🔁 Updated task '{update}' to '{up}'.")
                else:
                    print("❌ Task not found.")

            elif operation == 3:
                delete = input("Enter the task you want to delete: ")
                if delete in tasks:
                    tasks.remove(delete)
                    print(f"🗑️ Task '{delete}' has been deleted.")
                else:
                    print("❌ Task not found.")

            elif operation == 4:
                print(f"📋 Current tasks: {tasks}")

            elif operation == 5:
                print("👋 Closing the program...")
                break

            else:
                print("⚠️ Invalid Input. Please enter a number from 1 to 5.")

        except ValueError:
            print("⚠️ Invalid Input. Please enter a valid number.")

# Run the function
task()
