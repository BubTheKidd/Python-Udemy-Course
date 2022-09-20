# Function used to fuse Lists together in a
# Tuple format

engrams = ["Common", "Uncommon", "Rare", "Legendary", "Exotic"]
colors = ["White", "Green", "Blue", "Purple", "Yellow"]
# Primarily useful when converting multiple Lists into
# one Dictionary...
destiny_items = dict(zip(engrams, colors))
print(destiny_items)

# If two lists are different lengths, the Zip function
# will ignore the longer elements so that the lists
# match up