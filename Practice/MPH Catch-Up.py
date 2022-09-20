# How long will it take for father to catch up???

# How fast are both cars going?

# How far away is the destination?


miles_to_destination = int(input("How many miles left until you reach your destination?"))

user_current_speed = int(input("How fast are you going? (in MPH)"))

uhual_current_speed = int(input("How fast is the uHual currently going (also in MPH)"))

user_miles_per_minute = user_current_speed / 60 # Miles per minute driven...

uhual_miles_per_minute = uhual_current_speed / 60 # Miles per minute

user_reach_destinatiton = miles_to_destination / user_miles_per_minute # How many minutes till destination...

uhaul_reach_destination = miles_to_destination / uhual_miles_per_minute # Same

while(x != user_reach_destinatiton):
    x += user_miles_per_minute

user_distance_traveled = 0

uhual_distance_traveled = 0
    
# Find point they intersect (in miles)
# How long did it take each car to reach point?
# Measure in minutes, easier to track...

