# The @property allows for methods to be called as if they were a
# property of the class itself!


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []


    def average(self):
        return sum(self.grades) / len(self.grades)



class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
        
    # Only use when calculating an objects properties by itself
    @property
    def weekly_salary(self):
        return (self.salary * 40)
        

# Instantiation of new object
student = WorkingStudent("Billy", "Pine Creek", 12)


# A simpler way of calling simple functions 
# allowed through the use of @property
print(student.weekly_salary)
