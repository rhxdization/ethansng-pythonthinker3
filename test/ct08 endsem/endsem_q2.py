import os
import string

"""
============================================================
Q2. Review Text Analysis
============================================================
You are given a text file containing customer reviews.
The program must analyse the reviews and generate a rating.

Program Requirements:
- Read the contents of the file "reviews.txt"
- Count the total number of characters in the file
- Count how many reviews contain "good"
- Count how many reviews contain "bad"
- Calculate the percentage of good reviews
- Determine the overall rating:
    70% and above → Positive
    40% to 69% → Mixed
    Below 40% → Negative
- Save the results into "review_results.txt" and also print the results to the console

Note:
- The counting must be case-insensitive
- The percentage must be rounded to 2 decimal places
- If there are no valid reviews, the percentage should be 0

Print and save the result in this format:
    Review Text Analysis
    ------------------------------
    Total Characters: <number>
    Good Reviews: <number>
    Bad Reviews: <number>
    Percentage of Good Reviews: <value>%
    Overall Rating: <rating>

============================================================
"""

# ============================================================
# Step 1: Read file contents
# ============================================================

counter = 0
good = 0
bad = 0
words = []
variable = []
filepath = os.getcwd()
filepath = os.path.join(filepath, "test", "ct08 endsem", "reviews.txt")
print(filepath)
with open(filepath, "r") as f:
    content = f.read()
    for character in content:
        counter += 1
    f.close()
with open(filepath, "r") as f:
    content = f.readlines()
    for word in content:
        variable += word.split()
        for p in string.punctuation:
            variable = [i.replace(p, "") for i in variable]
    f.close()
for item in variable:
    print(item)
    if item.lower() == "good":
        good += 1
    elif item.lower() == "bad":
        bad += 1
    else:
        pass
        

    
    

# ============================================================
# Step 3: Count characters and good or bad reviews
# ============================================================



# ============================================================
# Step 4: Calculate percentage and rating
# ============================================================



# ============================================================
# Step 5: Write results to file
# ============================================================



# ============================================================
# Step 6: Print results to console
# ============================================================
