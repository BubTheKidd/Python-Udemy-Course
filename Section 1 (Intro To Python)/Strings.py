hello = "Hello World!"

print(hello)

# Strings take an assortment of characters surrounded
# by quotation marks

# Double or Single quotation marks can be used, but if
# if one is used in the string itself, the other must
# be used on the outside

first_example = "It's a me, Mario!"

second_example = '"Luigi looked away bashfully"'

print(first_example, second_example)

# You can also make multi-line strings

multi_example = """This is a string that
spans multiple lines. Quite fascinating really!
(Well, not really but it's cool enough...)"""

print(multi_example) # Printed exactly the same as written...

"""Can also just straight up create a string that
doesn't necassarily do anything. Great for multi-
line comments"""

name = "Jarod"

print("My name is: " + name)

# Can use the '+' symbol to concatenate strings...

age = 23 # Cannot concatenate integers with strings

string_age = str(age) # Must first convert it to a string

print("I am " + string_age + " years old!")

# Formatted strings however also exist within Python

print(f"That's right! I'm {name} and I'm {age} years old.")

# However, if the value in a formatted string is changed,
# that change wont be seen. Can be fixed by using the
# format() function...

greeting = "Hello {}, nice to meet you."

jarod_greeting = greeting.format(name)

print(jarod_greeting)

blue_greeting = greeting.format("Blue")

print(blue_greeting)

# Another way of using the format() function is...

alias = "Spider-Man"

catch_phrase = "Just your friendly, neighborhood {alias}"

print(catch_phrase)

# Kind of like making a "template" of sorts...

superhero_phrase = catch_phrase.format(alias = "Spider-Man")

print(superhero_phrase)

# Using the template, I inserted Spider-Man, but I could
# enter anything really

superhero_phrase = catch_phrase.format(alias = "Batman")

print(superhero_phrase)

# ...format(name of reference, variable or string being put in)

stuff = "Hello {}, what's {}?"

bleh = stuff.format("dude", "up")

print(bleh)

# All these formatting techniques can be used together!

