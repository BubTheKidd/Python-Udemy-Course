brother = "Ryker"
user_name = input("Enter your name: ")

# If condition evaluates to True, prints code
if user_name == brother:
    print("Hello Brother!")
# Else, prints a different set of code
else:
    print("Who are you???")

# Equivalent to running 5 through bool() 
if 5:
    print("""Is a whole number being passed through the bool() 
             so evaluates to true...""")


# This is slightly more useful for strings...
name = input("Enter your name forreal this time: ")
if name:
    print(f"Hello {name}")
# If nothing is typed in, returns False
else:
    print("Just tell me...")


superheroes = ["Spider-Man", "Batman", "Iron Man"]

user_alias = input("Enter your Super-Hero name: ")

# The "in" keyword is used to check if a value is in
# the superheroes list...
if user_alias in superheroes:
    print("Welcome to the team!")
else:
    print("Sorry, you d qualify...")

first_or_middle = input("Now enter your first or middle name: ") 

names = ["Nadia", "Christian", "Ryker", "Jarod"]
middle_names = ["Selene", "Wayne", "Lee", "Jaime"]

# Can also use "elif" (else if) to check additional conditions
if(first_or_middle in middle_names):
    print("Middle name selected")
elif(first_or_middle in names):
    print("First name selected")
else:
    print("Do I know you?")




