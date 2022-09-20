# When importing anything, it turns into a "Module".
import file_operations


# Can also import only a function from a file. This makes that function global to 
# the script. Have to be careful of functions with the same name though as that
# will cause a lot of problems...
from file_operations import ReadFile, SaveToFile


# If file that you're importing is in another directory, then you have to include
# the whole path...
import example_directory.example


# I see this a lot online. Where they have a variable that is only like
# two letters. I now know that these are modules...
file_operations.SaveToFile("Jarod", "names.txt")


example_directory.example.Hello()



"""
This is known as the script. Projects usally only have one script with
many modules on the side that support it.
"""