# Duplication when programming is a good way of knowing that something is 
# inefficient or redundant. Basically, the code can be improved. This is
# where inheritance comes in


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return self.grades / len(self.grades)


# This is an example of what NOT to do
"""
class WorkingStudent:
    def __init__(slef, name, school, salary):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        return self.grades / len(self.grades)
"""


# Will be a class that inherits from the Student class
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # super() calls the initilization method of the parent class 
        # (therefore, its properties)
        super().__init__(name, school)
        self.salary = salary

    # Classes allow you to override inherited functions. So instead of using
    # the parent classes' "average" function, Python will use this one!
    @property
    def average(self):
        return "Bootybootybooty"


college_student = WorkingStudent("Jim", "MIT", 7.25)
print(college_student.average)
# Prints out WorkingStudents' average()...



