
'''
    marks dict 
        - key is student name (str)
        - value is list of 4 marks 
'''

student_marks = {}


def add_student():
    name = input("Enter name of student : ")

    if name in student_marks:
        print("Name exist already")
        return

    marks = []
    for i in range(4):
        mark = float(input(f"Enter student marks in subject {i+1} : "))
        marks.append(mark)

    # add record of student
    student_marks[name] = marks


def highest_scorer():
    if len(student_marks) == 0:
        print("No student")
        return

    highest_scorer = ""
    highest_percent = 0

    for student in student_marks:
        percent = sum(student_marks[student])/4
        if percent > highest_percent:
            highest_percent = percent
            highest_scorer = student

    print(f"{highest_scorer} scored highest marks : {highest_percent}%")


while True:
    print("------MENU--------")
    print("1. Add student")
    print("2. View records")
    print("3. Find highest scorer")
    print("4. Exit")

    choice = input("Make a choice : ")

    if choice == "4":
        print("Exiting program")
        break
    elif choice == "1":
        add_student()
    elif choice == "2":
        print("Records")
        print(student_marks)
    elif choice == "3":
        highest_scorer()
    else:
        print("Make a valid choice")
