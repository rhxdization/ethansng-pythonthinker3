import random
# chr is number to letter
# ord is letter to number
password = ""
users = {}
choice = 0

print("welcome to the thing")
def thing():
    print("1: create a user")
    print("2: update password")
    print("3: login")
    print("4: see current users")
    print("5: exit")

while choice != 5:
    thing()
    choice = int(input("pick an option: "))
    if choice == 1:
        password = ""
        user = input("username: ")
        user2 = user.split()
        user = "".join(user2)
        if user in users:
            print("user already exists")
        else:
            for i in range(12):
                password += chr(random.randint(33, 126))
            users[user] = password
            print(f"user created! your password is {password}")
    elif choice == 2:
        user = input("username: ")
        if user not in users:
            print("user does not exist")
        else:
            verify = input("current password: ")
            if users[user] != verify:
                print("incorrect password")
            else:
                password = ""
                for i in range(12):
                    password += chr(random.randint(33, 126))
                users[user] = password
                print(f"password changed! your new password is {password}")
    elif choice == 3:
        user = input("username: ")
        if user not in users:
            print("user does not exist")
        else:
            verify = input("current password: ")
            if users[user] != verify:
                print("incorrect password")
            else:
                print("successfully logged in")
    elif choice == 4:
        for i in users:
            print(f"{i}: ************")
    elif choice == 5:
        print("bye")
        break
    else:
        print("type an option")