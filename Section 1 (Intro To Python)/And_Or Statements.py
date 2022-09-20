age = int(input("Enter your age: "))

can_read_books = age > 3 and age < 125

print(f"You can read at that age level: {can_read_books}")

# Can use the "and" keyword as well as the "or" keyword
# just as you'd expect. To add additional conditions
# to a test

# When using the "and" keyword, it can be used as kind of
# a shorthand "if statement"

x = True

y = x and 69 #If first value is true, returns second value

tennis_career_range = age > 18 or age < 60

print(f"You are in the prime age level to play tennis professionally: {tennis_career_range}")

# If first condition evaluates to false, it will then
# check the next condition. (Prints out whatever is
# true)...

name = ""

last_name = "Rodriguez"

print(name or f"Mr. {last_name}")

# Like using an, "If False" statement...

# In Python, some values evaluate automatically to
# either True or False

print(bool(0)) # Evaluates to false

print(bool("")) # Evaluates to false

print(bool(420)) # Evaluates to true

print(bool("Steven")) # Evaluates to true

# It seems that converting an empty value to a bool
# returns False whereas converting a value with anything
# in it returns True...

print(not True) # Prints the opposite

