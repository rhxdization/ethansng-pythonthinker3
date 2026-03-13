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
            name = input("What would you like your task to be named? ")
            if os.path.exists(f"{name}.txt"):
                print(f"Task file {name}.txt already exists.")
                confirmation = input("Overwrite? (y/n):").lower()
                if confirmation == "y":
                    file = open(f"{name}.txt", "w")
                    file.close()
                else:
                    print("ok")
                    continue
            else:
                file = open(f"{name}.txt", "w")
                file.close()
        elif choice == "2":
            print("2")
        elif choice == "3":
            print("3")
        elif choice == "4":
            print("4")
        elif choice == "5":
            print("5")
        elif choice == "6":
            break
        else:
            print("type something")

menu()