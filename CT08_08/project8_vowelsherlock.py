import os

filepath = os.getcwd()

fullpath = os.path.join(filepath,"sherlock.txt")

characters = 0
vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
nonvowels = 0
totalvowels = 0


if os.path.exists(fullpath):
    print("this file (sherlock.txt) exists".format(fullpath))
    with open("sherlock.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
            characters += len(line)
            for char in line:
                if char == "a":
                    vowels["a"] += 1
                    totalvowels += 1
                elif char == "e":
                    vowels["e"] += 1
                    totalvowels += 1
                elif char == "i":
                    vowels["i"] += 1
                    totalvowels += 1
                elif char == "o":
                    vowels["o"] += 1
                    totalvowels += 1
                elif char == "u":
                    vowels["u"] += 1
                    totalvowels += 1
                else:
                    nonvowels += 1
        print(f"Total characters: {characters}")
        print("Vowel counts in 'sherlock.txt':")
        for vowel in vowels:
            print(f"{vowel}: {vowels[vowel]}")
        print(f"Total vowels: {totalvowels}")
        print(f"Non-vowels: {nonvowels}")
        percentage = round(((totalvowels/characters) * 100), 2)
        print(f"Percentage of amount of vowels: {percentage}%")
else:
    print("no exist".format(fullpath))


