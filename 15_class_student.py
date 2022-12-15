
class Student:
    max_average = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = sum(marks) / len(marks)

        # Updating CLASS variable max_average using Student. notation not self.
        Student.max_average = max(Student.max_average, self.average)

    def display(self):
        print(f"Name : {self.name}")
        print(f"Marks : {self.marks}")
        print(f"Average: {self.average}")
        print(f"Class Max average : {self.max_average}\n")


george = Student("george", [4, 5, 2])
mili = Student("mili", [14, 5, 2])
corpse = Student("corpse", [4, 15, 2])

george.display()
mili.display()
corpse.display()
