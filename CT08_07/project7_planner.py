import os

filepath = os.getcwd()

def menu():
    choice = 0
    while choice != "6":
        print("Menu:")
        print("1. Create a new task file")
        print("2. View all tasks")
        print("3. Add a new task")
        print("4. Delete a task")
        print("5. Mark a task as done")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if os.path.exists(f"tasks.txt"):
                print(f"Task file tasks.txt already exists.")
                confirmation = input("Overwrite? (y/n): ").lower()
                if confirmation == "y":
                    with open("tasks.txt", "w") as file:
                        file.write("My Task List")
                    print("Successfully overwriten")
                    global counter
                    counter = 1
                else:
                    print("Overwrite cancelled")
                    continue
            else:
                with open("tasks.txt", "w") as file:
                    file.write("My Task List")
                    print("New task file written")
                    counter = 1
        elif choice == "2":
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
        elif choice == "3":
            task = input("Enter a new task: ")
            with open("tasks.txt", "a") as file:
                file.write(f"\n{counter}: {task}")
            counter += 1
        elif choice == "4":
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
                delete = int(input("Enter the task number to delete: "))
                if not isinstance(delete, int):
                    print("type an integer")
                else:
                    with open("tasks.txt", "r") as file:
                        lines = file.readlines()
                    lines = [line for line in lines if not line.startswith(f"{str(delete)}:")]
                    with open("tasks.txt", "w") as file:
                        counter = 1
                        for line in lines:
                            file.write(f"{counter}: {line}")
                            counter += 1

        elif choice == "5":
            print("5")
        elif choice == "6":
            break
        else:
            print("type something")

menu()