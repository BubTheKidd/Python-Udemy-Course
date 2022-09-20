# A Prime number is a number that can only be divided
# by 1 and itself

max = int(input("How many numbers would you like to test? (Excluding 1) ")) + 2

# Loop that is checking every number to see if Prime
for i in range(2, max):
    # Tests if 'i' is divisible by ANY number before it
    for x in range(2, i):
        if(i % x) == 0:
            # Showing how number is NOT Prime...
            print(f"{i} equals {x} * {i//x}")
            # The first time i is found to be Prime,
            # it stops testing numbers...
            break
    # Runs if for loop is not broken...
    else:
        print(f"{i} is Prime!")

    # If the encapsulated loop used the "continue" keyword
    # instead of "continue", then it would just keep running
    # the inside loop until it was finished each time. Meaning
    # this code would run for much too long and lose its
    # functionality...
