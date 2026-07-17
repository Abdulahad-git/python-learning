student = [
    {"name": "alice","score": 88},
    {"name": "abdul","score": 90},
    {"name": "ashik","score": 70},
    {"name": "ram","score": 73}
]
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

for s in student:
    print(s["name"], s["score"],
calculate_grade(s["score"]))