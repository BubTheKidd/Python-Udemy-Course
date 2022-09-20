# One of the most popular file types in the world
# JSON = JavaScript Object Notation
# Python Dictionary == JavaScript Object


import json


friends_file = open("Section 6 (Files In Python)\JSON Files\\friends_json.txt", 'r')
# Reads the json file and turns into a Python Dictionary
friends = json.load(friends_file)
friends_file.close()
print(friends["friends"])


heroes = [
    {"Name": "Spider-Man", "Power": "Spider-Powers"},
    {"Name": "Batman", "Power": "Money"}
]

heroes_file = open("Section 6 (Files In Python)\JSON Files\heroes_json.txt", 'w')
json.dump(heroes, heroes_file, indent = 4)
heroes_file.close()