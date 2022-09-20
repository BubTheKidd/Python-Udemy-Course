engrams = ["Common", "Uncommon", "Rare", 
                "Legendary", "Exotic"]

user_drops = input("What item rarity did you get?? ")

if(user_drops in engrams):
    print("Nice pull!")
else:
    print("That's not an item rank.")



shoe_companies = ["Nike", "Addidas", "Vans", "Sketchers"]

favorite_shoes = input("What's your favorite kind of shoe? ")

if(favorite_shoes.capitalize() in shoe_companies):
    print(f"{favorite_shoes} is indeed one of your favorite shoes...")
else:
    print("That isn't an available shoe company...")



# Made a couple of lists and integrated some easy list
# comprehension techniques...
good_names = ["Steven", "Jarod", "Jarvis", "Peterson"]

bad_names = ["Jervais", "Ryker", "Pickle Rick"]

your_name = input("Input your name. I'll see if your name is good enough...")

if(your_name.capitalize() in good_names):
    print("That is a fine name indeed!")
elif(your_name.capitalize() in bad_names):
    print("That name SUCKS....")
else:
    print("Meh, it's a name.")



# Made different lists for if the user puts in lowercase
# or uppercase variants of the answer
fantasy_names = ["Eivor", "Geralt", "Faendal"]
lower_fantasy_names = [name.lower() for name in fantasy_names]
upper_fantasy_names = [name.upper() for name in fantasy_names]
user_name = input("Enter your fantasy name: ")
if(user_name in fantasy_names or lower_fantasy_names or upper_fantasy_names):
    print("Hello person of ye old. ")
else:
    print("You don't belong here...")



# Doesn't work because the lowercase version of the
# answers don't exist and therefore, can't be checked
"""
# Is there a way to shorten the code above???
fantasy_names = ["Eivor", "Geralt", "Faendal"]
user_name = input("Enter your favorite fantasy name: ")
if((user_name in fantasy_names) or (user_name.lower() in fantasy_names) or (user_name.upper() in fantasy_names)):
    print(f"{user_name} is a great fantasy name!")
else:
    print("That's not a viable name...")
# Slightly more efficient? (Less code...)
"""


