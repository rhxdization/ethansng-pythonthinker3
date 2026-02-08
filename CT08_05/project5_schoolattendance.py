## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.

students = {
    "jonny": [True, True, True],
    "sally": [False, False, True],
    "becky": [False, True, True],
    "mark": [True, True, True],
    "linda": [False, False, False]
}

# ## Task 2: Take Student Attendance
# **Take Attendance​**

# Create a function called take_attendance()​

# Params:​
# - dictionary containing the student name and previous attendance​

# Function purpose:​
# - Loop through all the students, and ask if the student present or absence, and update the attendance accordingly.​
# - You must validate the input.​

# Return:​
# - updated dictionary with attendance record

def takeattendance(students):
    for i in students:
        answer = input(f"{i} is present?: ")