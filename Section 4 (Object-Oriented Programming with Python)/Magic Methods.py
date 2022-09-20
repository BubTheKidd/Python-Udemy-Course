# These are methods that you can add to a class (therefore, an object) to
# add increased functionality to an object (adding len() or [index]
# capabilities for example...)


# Dunder functions == Magic methods
class Guardian:
    def __init__(self, subclass):
        self.subclass = subclass
        self.inventory = ["Sunshot", "The Colony", "Traveler's Chosen"]

    # Used to be able to index lists in object
    def __getitem__(self, index):
        return self.inventory[index]

    # Adds len() functionality to objects
    def __len__(self):
        return len(self.inventory)

    # Used to represent the current object (better for
    # code-oriented representation)
    def __repr__(self):
        # This magic method is preferred over __str__
        return f"<< {self.subclass}: {self.inventory} >>"

    # Used to print out a user-friendly string (user-oriented
    # representation)
    def __str__(self):
        return f"<<{self.subclass} has {self.inventory}>>"


# Everything in Python is basically an object...

warlock = Guardian("Warlock")

# 'Sweet' way of saying Guardian.__getitem__(warlock, index)
print(warlock[2]) 

# After defining the __getitem__ and __len__ functions, the ability to
# iterate over your object becomes available!
for item in warlock:
    print(item)


print(warlock)