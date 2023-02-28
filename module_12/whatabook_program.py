""" 
    Title: whatabook.py
    Author: Rebecca Robinson
    Date: 02.24.23
    Description: Full Whatabook program.
"""

# Imports.
import mysql.connector
import sys
import time
from mysql.connector import errorcode

# Database configuration.
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Welcome message and main menu.
def show_menu():
    print("\n Welcome to the Whatabook User Database")
    time.sleep(.5)
    print("\n Main Menu - Please Make a Selection")
    print("    1. View Books\n    2. View Store Locations\n    3. View Account\n    4. Exit Program")

    try:
        choice = int(input('\n    Please make a selection: '))
        return choice
    except ValueError:
        print("\n  Invalid selection. Please try again.\n")
        time.sleep(1.5)


def show_books(_cursor):
    # Inner join.
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    
    # Get results.
    books = _cursor.fetchall()

    print("\n  **Current Stock**\n")
    
    # Display results. 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  **Store Locations**\n")

    for location in locations:
        print("  Prime Location: {}\n".format(location[1]))

# Check user.
def validate_user():

    try:
        user_id = int(input('\n    Please enter your Customer ID (This should be a number between 1 and 3):  '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid selection. Your Customer ID is either 1, 2, or 3. Closing Program.\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid selection. Please try again.\n")
        time.sleep(1.5)

# Show user menu.
def show_account_menu():

    try:
        print("\n      **Customer Menu**")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid selection. Please try again.\n")
        time.sleep(1.5)

# Show user wishlist.
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        **Current Wishlist**")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

# Show available books that can be added to wishlist.
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        **Available Books**")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

# MySQL error check.
try:
    # Database connection and functions.
    db = mysql.connector.connect(**config)  

    cursor = db.cursor() 

    user_selection = show_menu() 

    # When not 4. 
    while user_selection != 4:

        # If 1, display books.
        if user_selection == 1:
            show_books(cursor)

        # If 2, show locations.
        if user_selection == 2:
            show_locations(cursor)

        # If 3, show users and account.
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                # Show user wishlist. 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # Show books to add to wishlist.
                if account_option == 2:

                    
                    show_books_to_add(cursor, my_user_id)

                     
                    book_id = int(input("\n        Please enter the book ID number you would like to add to your wishlist:"))
                    
                    # Add book to wishlist.
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # Commit changes to database.
                    db.commit() 

                    print("\n        Success! You have added Book id: {} to your wishlist.".format(book_id))

                # Invalid check. 
                if account_option < 0 or account_option > 3:
                    print("\n      This selection does not exist. Please try again.")

                # Show accounts. 
                account_option = show_account_menu()
        
        # Invalid check.
        if user_selection < 0 or user_selection > 4:
            print("\n  Invalid selection. Please try again.\n")
            time.sleep(1.5)
            
        # Show main menu.
        user_selection = show_menu()

    print('\n  Thank you for visiting. Remember, "To read is to voyage through time." \n                                                            -Carl Sagan ')

# Error management.
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Invalid username or password.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  This database does not exist.")

    else:
        print(err)

# Close database.
finally:
    db.close()
