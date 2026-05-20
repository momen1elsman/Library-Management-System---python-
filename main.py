
import os
library_catallog = {}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def add_book():
    while True:
        clear()
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        library_catallog[isbn] = {"title": title, "author": author, "available": True}
        print(f"Book '{title}' by '{author}' added with ISBN {isbn}.")
        choice = input("Add another book? (y/n): ").lower()
        if choice != "y":
            break

def check_out_book():
    while True:
        clear()
        isbn = input("Enter ISBN: ")
        if isbn in library_catallog:
            print("ISBN already exists")
            if library_catallog[isbn]["available"]:
                library_catallog[isbn]["available"] = False
                print(f"Book '{library_catallog[isbn]['title']}' checked out successfully.")
            else:
                print("Sorry, the book is currently checked out.")
        else:
            print("Book not found in the catalog.")
        choice = input("Check out another book? (y/n): ").lower()
        if choice != "y":
            break

def check_in_book():
    while True:
        clear()
        isbn = input("Enter ISBN to check in: ")
        if isbn in library_catallog:
            if not library_catallog[isbn]["available"]:
                library_catallog[isbn]["available"] = True
                print(f"Book '{library_catallog[isbn]['title']}' checked in successfully.")
            else:
                print("The book is already available.")
        else:
            print("Book not found in the catalog.")
        choice = input("Check in another book? (y/n): ").lower()
        if choice != "y":
            break

def list_books():
    while True:
        clear()
        print("\nLibrary Catalog\n")
        for isbn, book_info in library_catallog.items():
            print(f"ISBN {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")
        choice = input("Go to main menu? (y/n): ").lower()
        if choice != "y":
            break

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Check Out Book")
        print("3. Check In Book")
        print("4. List Books")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            check_out_book()
        elif choice == "3":
            check_in_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
