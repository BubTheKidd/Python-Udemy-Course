# Used to repeat things a defined amount of times
# Used to go over a collection of elements...

# More similar to foreach loops in other languages...

friends = ["Zach", "Talon", "David"]

# "friend" in this context is a new variable created 
# that stores the first value and then the next and
# the next and so on...
for friend in friends:
    print(friend)

# Using an _ in programming signifies that you are
# crating a variable that will never be used.
# Sort of a Temporary Variable if you will...
numbers = [0, 1, 2, 3, 4, 5]
for _ in numbers:
    print("Deez")

# Can use range() to determine amount of times run
for _ in range(6):
    print("Nuts")

# Can also print within a certain range of numbers
for index in range(3, 6):
    print(index)

# Can also do increments by adding a 3rd parameter
for index in range(1, 20, 2):
    print(index) # Prints every two numbers

# for _ in range(inclusive num, exclusive num, increment)

# The variable created by for loop can be used as the
# index for lists...
family_members = [
    {"name": "Ryker", "age": 20},
    {"name": "Christian", "age": 17},
    {"name": "Nadia", "age": 14}
]
for family in family_members:
    name = family["name"] # "family" replaces the 1st [] needed
    age = family["age"] # Same here
    print(f"{name} is {age} years old.")
