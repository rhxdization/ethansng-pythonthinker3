import os

filepath = os.getcwd()

fullpath = os.path.join(filepath,"encrypted_note.txt")
characters = []

if os.path.exists(fullpath):
    with open("encrypted_note.txt", "r") as file:
        note = file.read()
        file.close()
    for char in note:
        if char == ",":
            pass
        elif char == ".":
            pass
        else:
            characters.append(char.lower())
    with open("hidden_message.txt", "w") as file:
        for char in characters:
            file.write(char)
        file.close()
else:
    print("someone stole the note too bad i guess")