age = 23

is_over_age = (age >= 21)

is_under_age = (age < 21)

is_twenty_three = (age == 23)

print(f"User is over the age limit: {is_over_age}")

print(f"User is under the age limit: {is_under_age}")

print(f"User is 23 exactly: {is_twenty_three}")

# These are what's known as a boolean expression
# (The expression evaluates to either True or False)

secret_number = 69

user_number = int(input("Try to guess my secret number..."))

print(f"You were correct? {user_number == secret_number}")


