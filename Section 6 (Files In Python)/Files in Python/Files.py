# 'r' stands for "read only"
# Have to include the folder  due to how this workspace is configured...
# Also known as the Relative Path
data_file = open('Section 6 (Files In Python)\Files in Python\Data.txt', 'r')

# Interprets all the contents of the file into a single string
file_contents = data_file.read()

# There are only a certain amount of files that a computer can have open
# at a time, so you have to make sure to close your files
data_file.close()

# Already extracted info from "data.txt" so even though the file is closed,
# we can still print the info we grabbed
print(file_contents)


user_input = input("Write some stuff to put in the file: ")


# Have to be SUPER CAREFUL with 'w' or the 'write' mode as it overwrites 
# everything in the specified file...
data_file_writing = open('Section 6 (Files In Python)\Files in Python\Data.txt','w')

# Overwrites and inserts argument onto file
data_file_writing.write(user_input)
data_file_writing.close()
print(data_file_writing)