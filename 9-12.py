# DAY 9: DICTIONARIES, NESTING, AND THE SECRET AUCTION
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

def score_grader(dict):
    student_grades = {}
    for student in dict:
        if dict[student] >= 91:
            student_grades[student] = "Outstanding"
        elif dict[student] >= 81:
            student_grades[student] = "Exceeds Expectations"
        elif dict[student] >= 71:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"
    print(student_grades)

score_grader(student_scores)
