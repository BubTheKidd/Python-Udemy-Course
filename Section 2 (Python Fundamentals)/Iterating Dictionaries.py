destiny_subclasses = {"Warlock": "Shadebinder", "Hunter": "Bladedancer", "Titan": "Thundercrash"}

# Prints out the "Key"
for subclass in destiny_subclasses:
    print(subclass)

# Prints out the value attached to the "Key"
for subclass in destiny_subclasses.values():
    print(subclass)

# Prints the "Key" as well as its value (Tuples?..)
for character, subclass in destiny_subclasses.items():
    print(f"Class: {character}, Subclass: {subclass}")

""" So basically, you can choose which element from a 
    dictionary you want to iterate over, i.e. printing
    out only the keys or only the values (Or even both!)"""
