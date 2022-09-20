# Find who matched the most numbers with the winning
# lottery numbers and print their name, along with the 
# amount they won (winnings = 100 * len(numbers_matched))
import random

# List of players
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Creates winning lottery numbers Set
lottery_numbers = set(random.sample(range(22), 6))

most_winning_numbers = {}

# The variable 'index' becomes a representation of each dictionary
# in the 'players' List
for index in players:
    # The numbers associated with the player
    player_numbers = index['numbers']

    # All the players' numbers that match the winning lotto numbers
    player_numbers_matched = player_numbers.intersection(lottery_numbers)

    # Conditional for finding the player with only the MOST winning numbers
    if(len(player_numbers_matched) > len(most_winning_numbers)):
        most_winning_numbers = player_numbers_matched
        winning_player = index['name']
        
# How much money the player won based on amount of matching numbers
earnings = 100 ** len(most_winning_numbers) # ** is the exponent operator...

# Printing the results
print(f"The winning player with earnings of ${earnings} is {winning_player}.")