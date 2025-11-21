from data import STUDENT_LIST
import matplotlib.pyplot as plt

def plot_marks(name):
    for student in STUDENT_LIST:
        if student['name'].lower() == name.lower():
            print("Generating graph...")

            subjects = list(student['marks'].keys())
            marks = list(student['marks'].values())

            plt.bar(subjects, marks)
            plt.title(name+"'s Marks")
            plt.xlabel("Subjects")
            plt.ylabel("Marks")
            plt.show()
            return

    else:
        print("Student not found.")