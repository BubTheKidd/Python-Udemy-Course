# Used as a way to define boundaries in a list

friends = ["Zach", "Talon", "David", "Garrett"]

# users_list[non-inclusive start:inclusive ending]

# Will start after 2nd index and go up to 4th place
print(friends[2:4])

# Will print up to 3rd place in list
print(friends[ :3])

# Will start after 2nd index and go till the end
print(friends[2: ])

# Actually creates a new list with the same elements
print(friends[ : ])

# Starts x amount of spaces from the back
print(friends[-2: ])

# Can combine boundary techniques
print(friends[-2:3])

# [Start : Stop : Step]
# These are the 3 flags that List Splicing use...

    
