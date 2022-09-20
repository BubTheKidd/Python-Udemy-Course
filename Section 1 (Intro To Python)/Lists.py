friends = ["Zach", "David", "Talon"]

print(f"{friends[0]} is pretty good at art!")

# Functions the same as arrays in C# and tables in Lua

print(len(friends)) # Prints length of list

# Can nest lists inside of lists!?

friend_ages = [ ["Zach", 27], ["David", 25], ["Talon", 29] ]

print(f"One of my best friends is {friend_ages[1][0]}. He is {friend_ages[1][1]} years old!")

# Can also access values individually in nested lists

superheroes = [
    ["Spider-Man", "Webs"],
    ["Iron Man", "Tech"],
    ["Hulk", "Super-Strength"],
    ["Captain America", "Leadership"],
    ["Hawkeye", "Great Aim"]
] # Best to block out long lists like this...

skills = ["Smart", "Witty", "Willpower"]

skills.append("High Endurance") # Appends to list

print(skills)

skills.remove("Willpower") # Removes from list

print(skills)

# Can't remove nested value unless you do the whole 
# nested list

# Should only use Lists when you want to be able to 
# makes changes to a group of a values i.e. adding or
# removing values. Otherwise, using Tuples is more
# efficient...

# Using the join() function can make lists more readable
comma_seperated_list = ", ".join(friends)
print(f"My friends are {comma_seperated_list}.")

 