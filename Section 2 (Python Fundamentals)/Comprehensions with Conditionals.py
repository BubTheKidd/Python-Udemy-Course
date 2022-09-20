# Stores the temporary variable "age" in list,
# "odd_ages" for every number in "ages" that
# passes the conditional if statement...
ages = [21, 23, 25, 20, 26, 24]
odd_ages_1 = [age for age in ages if(age % 2 == 1)]
print(odd_ages_1)

# equivalent to...

odd_ages_2 = []
for age in ages:
    # If the remainder of the age isn't 0, than it's odd
    if(age % 2 == 1):
        # Manually attaching values on to the list
        odd_ages_2.append(age)
print(odd_ages_2)



# Can convert to sets to perform comparisons
ages_set = set(age for age in ages)
odd_ages_set = set(odd_age for odd_age in odd_ages_1)
print(odd_ages_set.intersection(ages_set))



"""What I'm doing up there is basically declaring a list (or set),
   as well as each value but in one single line. So you can
   block it up like: odd_ages_1 = age. Then age is defined
   after performing each iteration of arithmetic through the
   'ages' list... It's important that List Comprehensions make
   your code easer to read and more efficient. If it does the
   inverse, ask yourself if you really need it."""