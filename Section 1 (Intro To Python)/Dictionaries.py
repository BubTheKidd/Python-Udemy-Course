friend_personas = {
    "Zach": "Sepiroth", 
    "David": "Sonic",
    "Talon": "Moon Wizard",
    "Garret": "Falco"
    }

# Similar to tables in Lua where you can set a "key"
# and have a value associated with that "key". 

# Keeps the order in which you set the Dictionary

print(friend_personas["Talon"])

# Can set a key outside of initialization
friend_personas["Jarod"] = "Spider-Man"

print(friend_personas["Jarod"])

# Much like Sets, Dictionaries cannot contain duplicate
# keys...

# Can encapsulate Dictionaries inside of Tuples
# and Lists

friends = (
    {"name": "Zach", "age": 28},
    {"name": "Talon", "age": 30},
    {"name": "David", "age": 26}
)

# Grabs info at that index and then finds details
# from the specified key...
print(friends[0]["name"])

# A more readable way of doing this...
friend = friends[1]
print(friend["name"])

# Can also use the dict() function to turn data into
# a dictionary
family = [("Ryker", 20), ("Christian", 17), ("Nadia", 14)]
family_ages = dict(family)
print(family_ages["Ryker"])