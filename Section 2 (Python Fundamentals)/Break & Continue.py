# Making a list because values may change...
engrams = ["Rare", "Uncommon", "Legendary", "Exotic", "Legendary", "Rare"]

for engram in engrams:

    print(f"Drop: {engram}")

    # The "continue" keyword stops anything else from
    # running and automatically moves to the next 
    # iteration in the loop
    if(engram == "Uncommon"):
        print("Bro, what a terrible drop... let's keep going.")
        continue

    # The "break" keyword stops the loop....
    if(engram == "Exotic"):
        print("Nice drop!!! Let's go to orbit.")
        break

    # Doesn't run if the "continue" or "break" keywords
    # are used
    print("Booty Cheeks") # Effectively only runs twice... (The last two values are ignored)

