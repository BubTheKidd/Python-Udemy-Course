# Same process as List Comprehension, except it 
# removes need for a middle step therefore making
# it more readable...

# Original Process
family = ["Ryker", "Christian", "Nadia"]
friends = ["Zach", "Talon", "David", "Ryker"]
family_lower = set([name.lower() for name in family])
friends_lower = set([name.lower() for name in friends])
print(family_lower.intersection(friends_lower))

# New Process
family = ["Ryker", "Christian", "Nadia"]
friends = ["Zach", "Talon", "David", "Ryker"]
family_lower = {name.lower() for name in family}
friends_lower = {name.lower() for name in friends}
print(family_lower.intersection(friends_lower))

# The only difference here is that you are doing
# the comprehension in a set instead of a list. Can
# also do this with dictionaries...

school_friends = ["Jamie", "Rick", "Stevie"]
grades = [67, 94, 80]
friends_grades = {
    school_friends[i]: grades[i]
    for i in range(0, len(school_friends))
    }
print(friends_grades)