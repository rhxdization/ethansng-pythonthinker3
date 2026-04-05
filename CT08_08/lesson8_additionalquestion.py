# Vowel sherlock 6
# Count how many times a specific word appears in the text
# The program should ask the user to input a word to search for
# The search should be case-insensitive (e.g. "The" = "the")
# The program should ignore punctuation (e.g. "the," = "the")
# The program should only match whole words (e.g. "he" should not match "the")
# Input: a word entered by the user
# Output: number of times the word appears in the text
# Sample:
# Total characters: 52968
# Total vowels: 15705
# Vowel frequency:
# a = 3401
# e = 4835
# i = 2932
# o = 3227
# u = 1310
# Percentage of Vowels in Text: 29.65
#
#   
# the
#
# 'CT08_03the' appears 467 times in the text.

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
        word = input("what word would you like to find: ").lower()
        lines = file.readlines()
        for line in lines:
            