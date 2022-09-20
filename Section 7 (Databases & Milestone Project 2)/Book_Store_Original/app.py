# 1. Enter and retrieve book details
# 2. Mark books as read
# 3. Delete books from list
# 4. Write book info to books.txt
# Notes: Should have put separate functions within the books file to 
#        better space out the code/functionality


#---<Declaring>
menu = """
- Enter 'e' to enter a book
- Enter 'l' to list all books
- Enter 'r' to mark a book as read
- Enter 'd' to remove a book from list
- Enter 'q' to quit

>>> """
books_list = [
    {'name': "Witch Hat Atelier", 'author': "Kamomo Shirahama", 'read': True},
    {'name': "Hatsu Haru", 'author': "Shizuki Fujisawa", 'read': True}
    ]
#---^


#----------Main----------<
def Menu():
    StoreBooks() # Storing current books so there are no books from last execution
    user_input = ""
    while(user_input != 'q'):
        user_input = input(menu)

        if(user_input == 'e'):
            EnterBook()
        elif(user_input == 'l'):
            ListBooks()
        elif(user_input == 'r'):
            MarkBookRead()
        elif(user_input == 'd'):
            DeleteBook()


def EnterBook():
    user_input = ""
    while(user_input != 'q'):
        name = input("Enter the books title: ")
        author = input("Now its author: ")
        books_list.append({'name': name, 'author': author, 'read': False})
        user_input = input("Press any key to enter another book. Press q to go back to the menu: ")
    StoreBooks()


def ListBooks():
    with open("Section 7 (Databases & Milestone Project 2)\Book_Store_Project\\books.txt", 'r') as books_file:
        for line in books_file:
            print(line.strip())


def MarkBookRead():
    user_input = ""
    while(user_input != 'q'):
        user_input = input("Which book have you read?: ")
        for book in books_list:
            if(book['name'] == user_input):
                book['read'] = True
            else:
                print("Book not found...")


def DeleteBook():
    user_input = input("Which book will you delete?: ")
    for book in books_list:
        if(book['name'] == user_input):
            # This is considered BAD PRACTICE within Python. Iterating over the list itself is fine, but when
            # you remove elements from the list, Python can get confused and this can lead to errors...
            books_list.remove(book)
            StoreBooks() # Stores the new list that doesn't have the removed book


def JoseDeleteBook(name):
    global books_list
    books_list = [book for book in books_list if book['name'] != name]
    # Instead of iterating over the list and removing entries along the way, this method simply creates a new list
    # without the specified book and overwrites the old list. Much safer and more efficient.


def StoreBooks():
    with open("Section 7 (Databases & Milestone Project 2)\Book_Store_Project\\books.txt", 'w') as books_file:
        for book in books_list:
            books_file.write(f"Book Name: {book['name']} - Author: {book['author']} - Has Read: {book['read']}\n")
#----------Main----------^



JoseDeleteBook("Hatsu Haru")
print(books_list)

