# Create a Tuple
tuple_example = ("Fiona", "Abby", "Nadia")
print(tuple_example)

# Create a List
list_example = ["Apples", "Bananas", "Oranges"]
print(list_example)

# Create a Set
set_example = {"Finn", "Jake", "BMO"}
print(set_example)

# Create a Dictionary
dictionary_example = {"Finn": "Human", "Jake": "Dog", "BMO": "Video-Game"}
print(dictionary_example)

# Encapsulate a Dictionary within a Tuple
tupleception = ( {"Ryker": "Sucks"}, {"Nadia": "Stinks"}, {"Christian": "Deez"})
print(tupleception[0]["Ryker"])

# Encapsulate a Dictionary within a Set
"""Figured out that I can't do this..."""

# Encapsulate a Dictionary within a List
listception = [("Jarod", "Skinny"), ("Ryker", "Tall"), ("Christian", "Small")]
dict(listception)
print(listception[0])

# Can NOT make a Set or a List of dictionaries...
