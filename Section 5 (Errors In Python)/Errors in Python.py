# Errors in Python are what allow developers to effectively troubleshoot 
# their code. Learning how to read Tracebacks and the different KINDS of
# errors can be crucial in efficient programming...


# Produces a 'NameError' because the variable is not defined
print(empty_variable)

# Produces an 'IndexError' because the index called doesn't exist
aliens = ["Heatblast", "Diamondhead"]
print(aliens[3])

# Produces a 'KeyError' because the key is incorrect
heights = {"Jarod": "Tall", "Chloe": "Short"}
print(heights["Jarred"])

# Produces an 'AttributeError' because Lists can't .intersection()
family = ["Ryker", "Christian", "Nadia", "Fiona", "Abby"]
brothers = ["Ryker", "Christian"]
print(family.intersection(brothers))

# Produces 'NotImplementedError' when user attempts to use specified
# function...
def login(self):
    raise NotImplementedError("This feature is not yet available...")

# Produces 'RuntimeError'
"""Just an error that occurs when running your code. It is a pretty 
   generic error that isn't seen too often."""

# Produces 'SyntaxError' when syntax is used incorrectly
def WhatsGood:
    print("We're missing the parenthesis here!!!")

# Produces 'IndentationError' when indentation is missed
def BasicBitch():
print("Should be indented here...")

# Produces 'TabError' when different indentation is used (common
# when switching editors)
def Business():
  print("Stuff")

# Produces 'TypeError' when you use types incorrectly
print(5 + "Stuff")

# Produces 'ValueError'
print(int('6.9'))

# Produces 'ImportError'
"""When you have on file imported that import another file that 
   imports the file you are already using and it just becomes one
   big mess (import loop/circular import)"""

# Produces 'DeprecationWarning' when you want user to know that there
# is now a different, more accepted way of doing something...
from database import Database

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def Register(self, username, password):
        Database.write(self.username, self.password)
        raise DeprecationWarning("Still works, but is deprecated...")


    @classmethod
    def Register_User(cls, username, password):
        Database.write(username, password)
        return cls(username, password)
    
"""However, you won't need to use a lot of these warnings. You
   should just make your own exceptions..."""
