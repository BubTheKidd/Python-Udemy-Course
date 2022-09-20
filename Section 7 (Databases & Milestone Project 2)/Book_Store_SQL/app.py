import database
database.CreateBookTable()



def EnterBook():
    # Passes user input into a StoreBook() function
    name, author = input("Please enter the name: "), input("Now the author: ")
    database.StoreBook(name, author)


def DeleteBook():
    # Passes user input into a CreateNewListWithoutElement() function
    user_input = input("Which book do you want to remove?: ")
    database.RemoveBook(user_input)


def MarkRead():
    # Passes user input into a MarkAsRead() function
    user_input = ""
    while(user_input != 'n'):
        user_input = input("Which book did you read?: ")
        database.MarkAsRead(user_input)
        user_input = input("Would you like to mark another book as reaad? (y/n): ")


def ListBooks():
    # Calls the GrabAllBooks() and prints out a readable list for the user
    books = database.GrabAllBooks()
    for book in books:
        print(f"Name: {book['name']}, Author: {book['author']}, Has Read: {book['read']}")


def Menu():
    user_input = ""
    while(user_input != 'q'):
        user_input = input(menu_options)
        if(user_input in menu_selection):
            menu_selection[user_input]() # Brackets here make it so that the functions run!
        elif(user_input == 'q'):
            print("Goodbye!")
        else:
            print("Please choose from the available options...")


#-----<Menu Elements>
menu_selection = {
    'e': EnterBook,
    'd': DeleteBook,
    'r': MarkRead,
    'l': ListBooks
    # Functions won't run here unless brackets are added later to program
}

menu_options = """
Please select an option:
 - 'e' to enter a book
 - 'd' to delete a book
 - 'r' to mark a book as read
 - 'l' to list all books
 - 'q' to quit program

 >>> """
#-----^


Menu()