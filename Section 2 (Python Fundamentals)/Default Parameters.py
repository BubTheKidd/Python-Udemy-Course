# Uses Parameters
def Add(x, y):
    sum = x + y
    return sum

x = 6; y= 7

# Uses Arguments
sum = Add(x, y)

print(sum)


# You can set default values that run if no argument is passed in
def Multiply(x, y = 3):
    product = x * y
    return product

# Since no second value is passed in, Function will use default of 3
product = Multiply(2)

# Prints out 6
print(product)