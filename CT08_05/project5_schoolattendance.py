def takeattendence(students):
    for name, attendance in students.items():
        while True:
            att = input(f"is {name} here today? (y/n) ").lower()
            if att == "y":
                students[name].append(True)
                break
            elif att == "n":
                students[name].append(False)
                break
            else:
                print("Invalid input. Try again.")

def attendancepercent(students_dict):
    while True:
        student = input("which student would you like to check? ").lower()
        if student in students_dict:
            days = 0
            for attendance in students_dict[student]:
                if attendance == True:
                    days += 1
            percentage = days / 3 * 100
            print(f"student {student}'s attendance is {percentage}%")
            break
        else:
            print("wrong answer")



students = {
    "jonny": [],
    "sally": [],
    "becky": [],
    "mark": [],
    "linda": []
}

print("welcome to school attendance checker")
while input != "end":
    input = input("what would you like to do today (check attendance, take attendance, end): ").lower()
    if input == "check attendance":
        attendancepercent(students)
    elif input == "take attendance":
        takeattendence(students)
    else:
        print("no")






