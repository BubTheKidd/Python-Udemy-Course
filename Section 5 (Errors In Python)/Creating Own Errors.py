# Python has a lot of built-in rrrors, but also allows the programmer to 
# make custom errors...


class CustomError(TypeError):
    """
    This is a 'docstring', used for helping other Python developers understand
    your code and what it does. Must have triple quotations to be a docstring
    """
    def __init__(self, code, message):
        # TypeError takes in one 'str' argument, hence why we pass in a string
        super().__init__(f"Error Code {code}: {message}")
        self.code = code


# Can print out a docstring for any function that has one
error = CustomError(420, "Message...")
print(error.__doc__)
print(len.__doc__)


raise CustomError(716, 'Oops lol')


