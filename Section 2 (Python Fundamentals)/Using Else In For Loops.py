# You can use the "else" keyword in a for loop to run
# if it did not encounter any "break" keywords


# This should run 4 times successfully before breaking
# the code...
for i in range(1, 11):
    if(i == 5):
        print("Breaking code here...")
        break
    print("Running...")
# Using "else" here means it will only run if the loop
# isn't broken...
else:
    print("Successful build...")


# Also works with while loops...
age = 21
while(age < 25):
    print("You are still young!")
    age += 1
# There are no breaks found in the loop, so this code
# will run
else:
    print("You are now old...")

# Does "else" work with "continue" as well?
for i in range(1, 5):
    if(i == 3):
        print("Using continue here...")
        continue
    else:
        print("Else...")