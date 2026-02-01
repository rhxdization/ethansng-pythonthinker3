students = {
    "alice" : 75,
    "bob" : 85,
    "charlie" : 63
}

students["elias"] = 99
students["john"] = 56
students["kok seng"] = 65

# Try using an input() to ask which student you want to check the score for?
# What happens if you try accessing a student that does not exist?

input = input("enter the name of the student: ").lower()
if input in students:
    print(f"{input}'s score is: {students[input]}")
else:
    print(f"brodie who is {input} 😭")