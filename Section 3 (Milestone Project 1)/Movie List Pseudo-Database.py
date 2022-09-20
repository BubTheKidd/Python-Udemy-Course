# Goal is to write a program that allows the user to store movies
# in a List and look through that list as well. 

# Title, Director, and Year are some describers that can be used
# Need to create a menu for the user that allows them to choose what they
# want to be doing (search movies by title, add a movie, show all movies,
# or quit the program) 

# While loop and conditionals would serve well here...

# Using a List of Dictionaries

# Can use the "Pass" keyword as a placeholder for later code so you can
# keep programming the "framework" of your program

user_movies = [
    {"Title": "Balls", "Director": "Bub", "Year": "1998"},
    {"Title": "Booty", "Director": "Bub", "Year": "1998"},
    {"Title": "Deez", "Director": "Bub", "Year": "1998"},
]

user_input = 69

find_input = ""

def AddMovie():
    add_input = 69

    while(add_input != 0):
        # Grabbing movie data from user
        title = input("Enter the title of the movie: ")
        director = input("Enter the director of the movie: ")
        year = input("Enter the year it came out: ")

        user_movies.append({"Title": title, "Director": director, "Year": year})

        print("Movie has been added!")
        # This is giving an error because pressing Enter here cannot be turned into an integer...
        add_input = int(input("Press 0 to quit. Press any other number to keep adding. "))



def ListMovies():
        for movie in user_movies:
            print(movie)


# Jose made a ShowMovie() function to better output the Dictionary entry
# It was a formatted string that he also used in the FindMovie() function


def FindMovie():
    find_input = input("What movie are you looking for?: ")

    # Iterates through each element of user_movies
    for movie in user_movies:
        if(movie["Title"] == find_input):
            print("Movie Found!")
            print(movie)
            break
        else:
            print("Movie not found. Searching...")



while(user_input != 0):
    # The actual menu part of the loop
    print("Hello, welcome to your movie database! Choose an option: ")
    print("1: Add Movie \n2: List Movies \n3: Find Movie \n0: Exit")
    user_input = int(input())

    # Conditionals based on the user's input
    if(user_input == 1):
        AddMovie()
    elif(user_input == 2):
        ListMovies()
    elif(user_input == 3):
        FindMovie()
    elif(user_input == 0):
        break
    else:
        print("This is not an available option. Choose from the options listed.")

    
    # Instead of using a multitude of 'if' statements, you can instead use
    # a Dictionary to map all options to a function

    """
    user_options = {
        1 : add_movie,
        2 : list_movies,
        3: find_movie,
        0: exit
    }
    """
