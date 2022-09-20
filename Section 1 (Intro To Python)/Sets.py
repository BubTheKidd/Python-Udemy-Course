work_friends = {"Edward", "Angel"}

weekend_friends = {"Zach", "Talon", "Eugene", "Angel"}

# This creates an empty set (Like using {})
empty_set = set()

# Sets are very similar to Lists and Tuples, the main
# difference being that they have no order and cannot
# contain duplicate elements...

# Adds Garrett to the weekend_friends Set
weekend_friends.add("Garrett")

print(weekend_friends)

# Doesn't add anything because Garrett is already in the Set
weekend_friends.add("Garrett")

print(weekend_friends)

weekend_friends.remove("Eugene")

# You use Sets over Tuples or Lists because of their
# ability to easily be compared to other Sets...

# Searches for values that are in both Sets and
# removes them from specified Set...
only_weekend_friends = weekend_friends.difference(work_friends)

print(only_weekend_friends)

# Symmetric Difference is only the values that aren't
# shared

# Intersection is only the values found in both Sets

not_in_both = work_friends.symmetric_difference(weekend_friends)

print(not_in_both)

in_both = work_friends.intersection(weekend_friends)

print(in_both)

# Union is used to unite sets together into one big set

all_friends = work_friends.union(weekend_friends)

print(all_friends)

"""A good example of using Sets would be in a lottery
    game setting. One Set could contain the winning 
    numbers and another would contain the numbers of
    the player. You could then use the Set operations
    to compare these Sets together and see if the player
    has "Won" the game!"""