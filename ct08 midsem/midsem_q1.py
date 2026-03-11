answer_key = ["A","B","B","A","A","C","C","A"]
student_ans = ["B","C","D","B","C","A","C","A"]

def score_quiz(answer_key,student_ans):
    score = 0
    for item in range(len(answer_key)):
        if student_ans[item] == answer_key[item]:
            score += 1
    return score

def wrong_questions(answer_key,student_ans):
    list = []
    for item in range(len(student_ans)):
        if student_ans[item] != answer_key[item]:
            list.append(item+1)
    return list

def grade(score, total):
    if total == 0:
        total = 1
    percentage = (score / total) * 100
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

score = (score_quiz(answer_key,student_ans))
list = wrong_questions(answer_key,student_ans)
print(f"Score: {score}/{len(answer_key)}")
print(f"Wrong questions: {list}")
print(f"Grade: {grade(score, len(list))}")