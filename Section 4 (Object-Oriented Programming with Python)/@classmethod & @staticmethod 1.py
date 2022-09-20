# These decorators are used when you want to either pass in the class
# itself as an argument or when you want no parameters at all...


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []


    def average(self):
        return sum(self.grades) / len(self.grades)


# Classes don't REQUIRE an __init__() but they can't have properties
# without one
class Foo:
    # Decorator that passes the class in as an argument
    @classmethod
    # 'cls' stands for class and represents the class being used with the
    # @classmethod decorator
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()


class Bar:
    # Decorator that doesn't take any arguments as it has no parameters
    @staticmethod
    def hi():
        print("No arguments here!!!")

another_object = Bar()
another_object.hi()