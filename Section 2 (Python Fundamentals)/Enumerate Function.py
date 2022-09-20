# Function used to assign numerical values to 
# members of a List

friends = ["Zach", "Talon", "David"]


# Typical, inefficient way
index = 0
for friend in friends:
    print(f"{index}: {friend}")
    index = index + 1


# Using Enumerator
for index, friend in enumerate(friends):
    print(f"{index}: {friend}")


# Don't beat yourself up over not getting the most 
# efficient answer. Just solve the proble first and
# then refactor. Remember what Garrett taught you...