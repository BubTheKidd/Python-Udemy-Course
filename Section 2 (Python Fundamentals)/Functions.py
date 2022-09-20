# Functions start with the 'def' keyword because
# you're defining a function

def greeting():
    print("Hello")

greeting() 

# Functions also take parameters and arguments, same
# as C#...

# Can pass in a List as an argument
bullshit_list = ["Deez", "Dose", "Dumba"]

def stupid(bullshit):
    print(bullshit[0])
    print(bullshit[1])
    print(bullshit[2])

stupid(bullshit_list)

# Or...

# Can pass in a dictionary as well
bullshit_dictionary = {"Cannon": "Fodder", "Bantha": "Fodder", "Peas": "Carrots"}

def more_bullshit(bullshit):
    print(bullshit["Cannon"], bullshit["Bantha"], bullshit["Peas"])

more_bullshit(bullshit_dictionary)


# Having a variable inside of a function makes it local to that
# function alone...


transformers = [
    {"Name": "Optimus Prime", "Side": "Autobot", "Vehicle": "Semi-Truck"},
    {"Name": "Bumblebee", "Side": "Autobot", "Vehicle": "Beetle"},
    {"Name": "Starscream", "Side": "Decepticon", "Vehicle": "Jet"}
]

# Argument name can be the same as iterative in a simple case like this
def GoodOrBad(transformer):
    if(transformer["Side"] == "Autobot"):
        print("This Transformer is good!")
    else:
        print("This is an evil Transformer indeed...")

# Can use a For loop to use the function on each Dictionary in the 
# 'transformers' List
for transformer in transformers:
    GoodOrBad(transformer)
