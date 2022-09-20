# Without List Comprehension
integers = [1, 3, 5, 7, 9]
doubled_integers = []
for integer in integers:
    # Have to use the append() function to do it
    # this way...
    doubled_integers.append(integer * 2)
print(doubled_integers)
# Doubles every value in "integers" and
# appends it to new list "doubled_integers"

# With List Comprehension
doubled_integers = [(integer * 2) for integer in integers]
print(doubled_integers)
# Performs arithmetic (integer * 2) for every integer
# found in the "integers" list

# another example...

# Without List Comprehension
numbers = [1, 2, 3, 4, 5]
doubles = []
for number in numbers:
    doubles.append(number * 2)
print(doubles)

# With List Comprehension
new_numbers = [66, 417, 663]
meme_numbers = [(every_number + 3) for every_number in new_numbers]
# Stores the loop as well as the list inside the "meme_numbers" varaible
print(meme_numbers)

# Can also do it like this...

# Using range() function to replace list...
quintuple_numbers = [(i * 5) for i in range(10)]
print(quintuple_numbers)

# Another Example...
friends_ages = [23, 27, 31, 36]
# Not working because it's not in a list
ages_string = print(f"Friends Age: {age}" for age in friends_ages)
print(ages_string)
# Defining a new list and then, printing it
ages_string = [f"Friend's Age: {age}" for age in friends_ages]
print(ages_string)

names = ["Fiona", "Abby", "Nadia"]
lowercase_names = [name.lower() for name in names]
print(lowercase_names)



# List Comprehensions always create a new list