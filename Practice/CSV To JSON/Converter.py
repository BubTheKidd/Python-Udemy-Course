import json


# 1. Read data from csv_file.txt
# 2. Process data and convert them into a JSON object (list of dictionaries)
# 3. Store the object in the json_file.txt


csv_list = []


# Read data from csv_file.txt
csv_file = open("Practice\CSV To JSON\csv_file.txt", 'r')
csv_contents = [line.strip() for line in csv_file.readlines()]
csv_file.close()


# Convert into JSON object
for line in csv_contents:
    csv_contents = line.split(',')
    csv_list.append({"club": csv_contents[0], "city": csv_contents[1], "country": csv_contents[2]})


# Store the object in json_file.txt
json_file = open("Practice\CSV To JSON\json_file.txt", 'w')
json.dump(csv_list, json_file, indent = 4)
json_file.close()

