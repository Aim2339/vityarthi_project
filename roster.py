from data import STUDENT_LIST

def class_roster():
    count = 1
    print("\nClass Roster: ")
    for student in STUDENT_LIST:
        print(count, student['name'])
        count += 1