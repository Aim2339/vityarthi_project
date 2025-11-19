from reports import report_card
from visualize import plot_marks
from roster import class_roster


print("Teacher's Gradebook: ")
print("1. View Class Roster")
print("2. View Student Report Card")
print("3. Visualize Student Marks")
choice = input("Please choose an option (1-3): ")

if choice == '1':
    class_roster()

elif choice == '2':
    name = input("\nEnter student name: ")
    report_card(name)

elif choice == '3':
    name = input("\nEnter student name: ")
    plot_marks(name)
else:
    print("Please enter a number from 1 to 3.")