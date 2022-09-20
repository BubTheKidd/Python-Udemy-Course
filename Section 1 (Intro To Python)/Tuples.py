a_tuple = ("Zach",  "Talon", "David")

unclear_tuple = "John", "Marmot"

# Can create a tuple inside a list using parenthesis
tuple_inside_list = [("Nadia", "Christian")]

# Tuples should only be used when you need a group of
# values that won't change.

# Doing this technically just creates another tuple
a_tuple = a_tuple + unclear_tuple

print(a_tuple)

# Similar to how "changing" a string in C# just creates
# another string. This just adds to the memory and is
# considered inefficient...

# Tuples can be encapsulated within eachother
tuple_test = (("Stuff", "Meh"), ("Stupid", "What"), ("Test", "Maybe"))
print(tuple_test[0])

# Tuples are IMMUTABLE

# The equivalent to a Constant Variable (In this case, a group
# of constants...)