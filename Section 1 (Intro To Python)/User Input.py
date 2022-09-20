name = "Jarod"

user_name  = input("Enter your name: ")

print(f"Hi {user_name}, I'm {name}!")

# Anything the user types in using the input() function
# is considered a string in Python

age = input("Enter your age: ") #Dynamic Value

# Must first convert user's input into the desired
# data type...

age_num = int(age)

age_in_months = age_num * 12

print(f"You are {age_in_months} months old {user_name}.")

# Can also be done in one line...

age = int(input("Enter your desired age: "))

print(f"You are now {age} years old. Congratulations!")

# Important for variables to have good, descriptive names


 