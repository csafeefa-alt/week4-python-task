def validate_answers(student_answers, answer_key):
    correct = 0
    for i in range(len(answer_key)):
        if student_answers[i].lower() == answer_key[i].lower():
            correct += 1
    return correct
def calculate_score(correct_answers, total_questions):
    score = (correct_answers / total_questions) * 100
    return score
def generate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
answer_key = ['a', 'c', 'b', 'd', 'a']
student_answers = []
n = len(answer_key)
for i in range(n):
    ans = input(f"Enter answer for question {i+1}: ")
    student_answers.append(ans)
correct_answers = validate_answers(student_answers, answer_key)
score = calculate_score(correct_answers, n)
grade = generate_grade(score)
print("Correct Answers:", correct_answers)
print("Score:", score)
print("Grade:", grade)