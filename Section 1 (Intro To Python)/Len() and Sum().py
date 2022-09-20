grades = [80, 75, 90, 100]

# Can use the sum() and len() functions to get the total
# of a list as well as the length of it respectively
total = sum(grades)
length = len(grades)

average = total / length

print(f"Total: {total}")
print(f"Length: {length}")
print(f"Average: {average}")

# Which of these would be the worst for a grading system?
grades = [80, 75, 90, 100]
grades = (80, 75, 90, 100)
grades = {80, 75, 90, 100}

# Can add on to lists so wouldn't be the worst option
grades = [80, 75, 90, 100]

# Can't add on to a Tuple so not ideal
grades = (80, 75, 90, 100)

# Sets are the worst because you wouldn't be able to have
# two of the same grades
grades = {80, 75, 90, 100}


