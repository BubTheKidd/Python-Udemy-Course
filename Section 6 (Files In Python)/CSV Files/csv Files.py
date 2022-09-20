csv = open("Section 6 (Files In Python)\CSV Files\CSV Data.txt", 'r')
csv_data = csv.readlines()
csv.close()

# Using the strip() here so that we're not changing more than what we're gonna
# use (the 1st line that we've chosen to ignore...)
csv_data = [eachline.strip() for eachline in csv_data[1:]]

for eachline in csv_data:
    # title() capitilizes first letter of every word, capitalize() does only the
    # first letter
    person_data = eachline.split(',')
    name = person_data[0].title()
    age = person_data[1] # A way to remove repetition???
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f"{name} is {age} years old and is a {university} student studying {degree}")


joined_csv = ','.join(person_data)
print(joined_csv)
