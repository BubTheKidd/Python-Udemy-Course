# Can't use Math operators. Must use built in Addition module...
# Must have functions for add, subtract, multiply, and divide
from Addition import Addition


class Calculator():
    # Takes in a Class as well as two arguments...
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)   

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -(num2))

    # Why is this a @classmethod?
    @classmethod
    def multiply(cls, number, multiplier):
        # Use some sort of loop to repeatedly add numbers together?
        total = 0
        for i in range(0, multiplier):
            total = cls.add(number, total)
        return total

    @classmethod
    def my_divide(cls, dividend, divisor):
        quotient, divisor_added = 0, 0
        while True:
            # If tries to divide a small number by a big, return 0
            if(divisor > dividend):
                return 0

            # Returns quotient when you've reached the max amount of times it can go in
            elif(cls.add(divisor_added, divisor) > dividend):
                return quotient

            # If none of the conditions above are met, keep performing calculations
            else:
                divisor_added = cls.add(divisor_added, divisor)
                quotient = cls.add(quotient, 1)


    """
    The divide function gave me a lot of trouble here because of the way it was set up. It
    kept running an extra time and although I knew it had to do with the while() condition I
    had set up, I couldn't figure it out. Then I realized I didn't have to wait for my result 
    to go passed my parameters. I could use the add() in an if statement to give my code a 
    "glimpse into the future" so to speak. So, if 'divisor_added' would end up being more than
    the 'dividend' on the next iteration, than stop the loop right then and there...
    """

    @classmethod
    def their_divide(cls, dividend, divisor):
        res = 0
        while dividend >= divisor:
            dividend = cls.subtract(dividend, divisor)  # subtract divisor from dividend until its remainder is smaller than divisor
            res = cls.add(res, 1)   # count the times of subtraction as the result
        return res
