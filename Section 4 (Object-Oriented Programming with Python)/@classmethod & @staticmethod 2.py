"""A @staticmethod does not require an implicit 1st argument (does not
   require a 'self' parameter because the function will be bound to the
   class itself). Basically, making it Static just makes it a global
   function...effectively"""


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        # The '.2f' here allows for Python to print out to 2 decimal places
        return f"<< FixedFloat {self.amount:.2f} >>"

    # This function passes the result back up to the __init__() and becomes
    # the 'amount'...
    @staticmethod
    def floats_sum(value1, value2):
        return FixedFloat(value1 + value2)

    @classmethod
    def other_sum(cls, value1, value2):
        return cls(value1 + value2)

    
# Creating an empty object here for the sole purpose of using FixedFloat's
# class method to create yet another object is somewhat redundant
number = FixedFloat(17.4738)
other_number = number.floats_sum(16.549, 4.006)
print(other_number)


# Instead, the @staticmethod decorator should be used. Then, the method 
# becomes bound to the class, not the object being created...
another_number = FixedFloat.floats_sum(16.549, 4.006)
print(another_number)


# Class that builds off of the FixedFloat class. Prints out an amount of
# money in the currency of Euro (and cuts all decimal places at the 2nd 
# place because of the inherited FixedFloat class)
class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f"<< Euro: {self.symbol}{self.amount} >>"


money = Euro.other_sum(13.532, 5.5532)
print(money)

"""A @classmethod is used when you instead want to make a function 
   using a Class as a parameter (instead of an object). It is recommended
   to generally use the @classmethod decorator as the @staticmethod just
   isn't as useful... (It's just removing functionality whereas @classmethod
   does everything static does and more...)"""





