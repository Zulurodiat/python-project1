def calculate_average(scores):
    total = 0
    for score in scores:
        total = total + score

    average = total / len(scores)
    return average

students = [
    {"name": "Barakat", "scores": [50, 60, 70]},
    {"name": "Ola", "scores": [20, 45, 55]},
    {"name": "Ade", "scores": [70, 80, 95]}
    ]

for student in students:
    average = calculate_average(student['scores'])
    print(f"Ada's average score is {average}")

    if average >= 70:
        print("pass")
    else:
        print("fail")