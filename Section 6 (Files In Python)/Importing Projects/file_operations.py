def SaveToFile(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def ReadFile(filename):
    with open(filename, 'r') as file:
        return file.read().split()


"""
This is what's known as a module. Projects can have multiple modules and
these modules are used for importing into one main file, usually called app.py.
"""

    