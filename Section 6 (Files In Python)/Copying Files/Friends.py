# Ask user for list of 3 friends
# Inform the user whether each friend is nearby
# If they are, save their name to the nearby_friends file

print("Enter 3 of your friends!")

# Creates a list full of 3 of the users' friends...
friends = []
for i in range(1, 4):
    friends.append(input(f"Friend {i}: "))

# Opening up the 'people.txt' file and copying its contents to a variable
people = open("Section 6 (Files In Python)\Copying Files\people.txt", 'r')
# Reading what's currently in the file
people_nearby = [line.strip() for line in people.readlines()]

people.close()

# Putting the data into a Set so we can use the intersection method
people_nearby_set = set(people_nearby)
# Doing the same with 'friends'
friends_set = set(friends)
# Now intersecting them...
friends_nearby_set = friends_set.intersection(people_nearby_set)


print(people_nearby_set)
print(friends_set)

friends_nearby_file = open("Section 6 (Files In Python)\Copying Files\nearby_friends.txt", 'w')

# Printing out friends nearby and writing their names to the appropriate file
for friend in friends_nearby_set:
    print(f"{friend} is nearby!")
    friends_nearby_file.write(friend)

friends_nearby_file.close()

