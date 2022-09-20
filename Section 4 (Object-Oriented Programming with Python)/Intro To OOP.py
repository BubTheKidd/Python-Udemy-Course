student = {
    "name": "Jarod",
    "grades": [88, 91, 45]
}


# VERY inefficient...
def My_Average(grades):
    total = 0
    counter = 0

    for grade in grades:
        total += grade
        counter += 1

    return (total / counter)    
   
# Only one line of code making it very efficient
def Their_Average(student):
    return sum(student["grades"]) / len(student["grades"])


"""
The code here is good but there is a major flaw in this code's design.
The Average() function here works well with the 'student' Dictionary, but
it shouldn't DEPEND on it. It should have variables that are completly
independent and just allow for ambiguous data to be passed through (in case
you wanted to use the function for something BESIDES calculating student
grade averages...)
"""

# Objects store data as well as actions relating to that data

class Student_Class:
    # Dunder Function (Double Underscore)
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def Their_Average(self):
        return sum(student[self.grades]) / len(student[self.grades])

    def Print_Info(self):
        return(f"<<{self.name}>> has {self.grades}")

# Classes work as a template, where you can use it to create new objects
# all from the same starting point. 'self' in the class represents an
# empty object and .name as well as .grades become equivalent to whatever
# the user passes in (they become object variables or, Properties)

new_kid = Student_Class("Billy", [91, 88, 100])
popular_kid = Student_Class("Jimmy", [65, 51, 72])

# Another dunder function used to identify if it is a class
print(new_kid.__class__)

print(new_kid.name)
print(popular_kid.name)

# When calling a function from a class, there are two ways this can be done

# Automatically takes new_kid as an argument. If more than one parameter
# is specified, than additional info will need to be passed up...
print(new_kid.Print_Info())

# Is technically what's happening above, just inferred
print(Student_Class.Print_Info(new_kid))