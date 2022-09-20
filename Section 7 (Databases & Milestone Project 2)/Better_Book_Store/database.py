# Stores information to our "database"
# CSV Format = name,author,read



# There seems to be a lot of repetition here... How do I fix that?
# -> Create a function to break it down. Have to remember what Garrett taught me!!!
# Repetition happening with opening files and iterations over the books...

def StoreBook(name, author):
    # Storing the user's book to a .csv file
    with open("Section 7 (Databases & Milestone Project 2)\Better_Book_Store\\books.csv", 'a') as books_file:
        books_file.write(f"{name},{author},0\n")
    print("Book stored!")


def _RewriteFile(books): # Underscore before function represents a Private Function in Python
    # Rewrites the books.csv file
    with open("Section 7 (Databases & Milestone Project 2)\Better_Book_Store\\books.csv", 'w') as books_file:
        for book in books:
            books_file.write(f"{book['name']},{book['author']},{book['read']}")

            
def RemoveBook(name):
    # Creating a new books list WITHOUT user-specified book and re-writing the .csv file to reflect that
    books = GrabAllBooks()
    books = [book for book in books if book['name'] != name]
    _RewriteFile(books)
    print("Book removed!")


def GrabAllBooks():
    # Creating a List from the .csv file and returning it
    with open("Section 7 (Databases & Milestone Project 2)\Better_Book_Store\\books.csv", 'r') as books_file:
        lines = [line.strip().split(',') for line in books_file.readlines()]

    return [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]


def MarkAsRead(name):
    # Setting 'read' value to true
    books = GrabAllBooks()
    for book in books:
        if(book['name'] == name):
            book['read'] = True
    _RewriteFile(books)
                   

