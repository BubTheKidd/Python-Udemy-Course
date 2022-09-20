for i in range(1, 101):
    # Checking this first because it won't run if
    # the one of the other conditions runs true
    if((i % 3 == 0) and (i % 5 == 0)):
        print("FizzBuzz")
        continue
    elif(i % 3 == 0):
        print("Fizz")
        continue
    # Can also use this method to find multiples...
    elif((i / 5).is_integer()):
        print("Buzz")
        continue
    else:
        print(i)