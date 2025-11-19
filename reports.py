from data import STUDENT_LIST

def class_roster():
    print("\nClass Roster: ")
    for student in STUDENT_LIST:
        print(student['name'])

def grade(marks):
    if 100 >= marks >= 95:
        return "S"
    if 95 >= marks >= 90:
        return "A"
    elif 90 > marks >= 80:
        return "B"
    elif 80 > marks >= 70:
        return "C"
    elif 70 > marks >= 60:
        return "D"
    else:
        return "F"

def report_card(name):
    for student in STUDENT_LIST:
        if student['name'].lower() == name.lower():

            print("\nReport Card for",student['name'])
            total = 0
            count = 0

            for subject, mark in student['marks'].items():
                print(subject,":",mark, grade(mark))
                total += mark
                count += 1

            average = total/count
            print(">> Average marks:",average)

            if average >= 70:
                print(">> Status: Pass")
            else:
                print(">> Status: Fail")
            return
    else:
        print("Student not found.")