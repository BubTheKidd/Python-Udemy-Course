# Running something a certain amount of times
for i in range(15):
    print("Deez")
    print(i)

# Can iterate over lists, tuples, sets and dictionaries

# Tuples
my_siblings = ("Fiona", "Abby", "Nadia", "Christian", "Ryker")
for sibling in my_siblings:
    print(f"This is my sibling {sibling}.")

# Set
my_family = {"Mom", "Dad", "Aunt", "Grandma"}
for member in my_family:
    print(f"I have a {member}.")

# List
engram_types = ["Uncommon", "Rare", "Legendary", "Exotic"]
print("Types of engrams:")
for engram in engram_types:
    print(engram)

# Dictionaries
my_weapons = (
    {"Uncommon": "Helios FR5"},
    {"Rare": "Ballyhoo"},
    {"Legendary": "Night Watch"},
    {"Exotic": "Salvation's Grip"}
)
# I did a Tuple of dictionaries here but this wouldn't
# be ideal because my list of weapons is always growing
for rarity, weapon in my_weapons:
    print(f"Rarity: {rarity}, Weapon: {weapon}")

# Just did a straight up dictionary here...
my_other_weapons = {
    "Legendary": "Scathelocke",
    "Exotic": "Sunshot"
    }
for weapon in my_other_weapons.values():
    print(f"My other weappons include: {weapon}")




