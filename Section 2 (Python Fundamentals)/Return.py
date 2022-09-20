# Can use the Return keyword to make a function actually
# return a value in its place



def Sum(num1, num2):
    # Function ends whenever it encounters the first successful return
    return (num1 + num2)

num1 = int(input("Enter a number: "))

num2 = int(input("Now another: "))

# Can put the result of the function within a variable
sum = Sum(num1, num2)

print(sum)



# Useful for breaking up functions that do more than they need to
# Like a Muliplication function that multiplies two numbers, but also
# grabs user input, prints out the result and shows the user how 
# multiplication works...



# All functions return 'None" by default, but this can be explicitly
# stated...
def Subraction(num1, num2):
    print(num1 - num2)
    return None