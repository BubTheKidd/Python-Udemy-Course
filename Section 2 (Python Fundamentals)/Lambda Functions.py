# Just like regular function, but a lot shorter. Better suited for
# functions that are only doing like one thing (and a simple thing
# at that!)


# Normal Function
def Normal_Divide(x, y):
    return x / y

# Lambda Function
Lambda_Divide = lambda x, y: x / y


# Normal Function Call
print(Normal_Divide(9, 3))

# Lambda Function Call
print(Lambda_Divide(9, 3))


# Lambda functions are better used when only wanting to perform
# a small amount of tasks...


def Average(seq):
    return sum(seq) / len(seq)

# To...

# Most of these are just "proxy functions" where they're not really
# doing anything different from the base functions used...
average = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"Name": "Rolf", "Grades": (69, 35, 58)},
    {"Name": "Suzan", "Grades": (98, 68, 12)},
    {"Name": "Chud", "Grades": (86, 91, 95)},
    {"Name": "Boomer", "Grades": (83, 0, 88)}
]

# Dictionary used to associate user input with the appropriate functions
operations = {
    "average" : average,
    "total" : total,
    "top" : top
}

# For Loop used to iterate over the 'student' List of Dictionaries
for student in students:
    name = student["Name"]
    grades = student["Grades"]

    print(f"Student: {name}")
    user_input = input("Would you like to calculate average, total or top grade for the student?")

    # "user_operation" becomes one of the Lambda funtions from above
    user_operation = operations[user_input]
    print(user_operation(grades))

    # This is one way of interpreting user input...
    if (user_input == "average"):
        print(average(grades))
    elif (user_input == "total"):
        print(total(grades))
    else:
        print(top(grades))

    # Instead of defining every possible input using if statements,
    # you can creaate a Dictionary where you 'associate' the possible
    # inputs (the Keys now) with the function they're tied to. This 
    # currently removes the ability to account for errors from the users'
    # side. Fixable later...

