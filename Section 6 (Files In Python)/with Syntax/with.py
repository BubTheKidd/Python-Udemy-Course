# With is what's known as a context manager. This keyword basically opens
# and closes files in one line.
import json


# Original Way:
file = open("Section 6 (Files In Python)\with Syntax\example json.txt", 'r')
file_contents = json.load(file)
file.close


# New Way:
with open("Section 6 (Files In Python)\with Syntax\example json.txt", 'r') as file:
    file_contents = json.load(file)
