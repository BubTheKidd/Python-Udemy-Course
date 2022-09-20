# This seems to be a function that is useful when dealing with
# Dictionaries and Strings alike...

test_dict = {
    "name": "Jarod",
    "age": 23,
    "ethicity": "Hispanic"
}

user_input = input("What data are you looking for? ")

print(test_dict.get(user_input, 'This data does not exist...'))

# Allows you to grab values from keys in a Dictionary and also allows you
# to set a default value in case the user's key can't be found...