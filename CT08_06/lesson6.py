answerkey = ["A", "D", "C", "D"]

studentanswers = {
    "John": ["A", "D", "C", "D"],
    "Joshua": ["A", "A", "C", "C"],
    "Jack": ["B", "C", "C", "D"],   
    "Jill": ["D", "C", "B", "A"],
}

def gradeallstudents(studentanswers, answerkey):
    test_scores = {}  
    for name, answers in studentanswers.items():
        print(name)
        print(answers)
        sum = 0
        for i in range(len(answerkey)):

            if answers[i] == answerkey[i]:
                sum += 1
        test_scores[name] = sum/len(answerkey)*100
    return test_scores


test_scores = gradeallstudents(studentanswers, answerkey)
print(test_scores)
def calculateavgscore(test_scores)



        


    
    

