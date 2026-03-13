import os
filepath = os.getcwd()

fullpath = os.path.join(filepath,"file.txt")


if os.path.exists(fullpath):
    print("it exist".format(fullpath))
else:
    print("no exist".format(fullpath))

file = open("manualoutput.txt", "r")
content = file.read()
print(content)
file.close