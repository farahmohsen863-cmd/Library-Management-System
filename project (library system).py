# -----------------------------------------
# Library Management System 
# Uses: Variables - Lists - Dicts - Loops - Conditions - Functions - OOP
# -----------------------------------------

# -----------------------------------------
# Book Class
# -----------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def show_info(self):

        print("\n---Book Info---")
        print("Title:", self.title)
        print("Author:", self.author)

        if self.available:
            print("Starus: Avilable")
        else:
            print("Status: Borrowed")

        print("------------------")


 # -----------------------------------------
 # List to store books
 # -----------------------------------------
books = []

# -----------------------------------------
# Add Book
# -----------------------------------------
def add_book():

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = Book(title, author)

    books.append(book)

    Library_info["total_books"] += 1

    print("Book added successfully")

# -----------------------------------------
# Show All Books
# -----------------------------------------
def show_all_books():

    if len(books) == 0:
        print("No books found.")
        return

    for b in books:
        n.show_info()

# -----------------------------------------
# Search Book
# -----------------------------------------
def search_book():

    title = input("Enter book title: ")

    for b in books:
        if b.title.lower() == title.lower():
            b.show_info()
            return

    print("Book not found.")

# -----------------------------------------
# Delete Book
# -----------------------------------------
def delete_book():
    title = input("Enter book title to delete: ")
    

    for b in books:
        if b.title.lower() == title.lower():

            books.remove(b)

            library_info["total_books"] -= 1

            print("Book deleted successfuly.")
            return
    print("Book not found.")    
        

     

# -----------------------------------------
# Borrow Book
# -----------------------------------------
def borrow_book():

    title = input("Enter book title to borrow: ")
 
    for b in books:

        if b.title.lower() == title.lower():

            if b.available:
                b.available = False
                print("Book borrowed successfuly.")
            else:
                print("Book already borrowed.")

            return

    print("Book not found.")

# -----------------------------------------
# Return Book
# -----------------------------------------
def return_book():

    title = input("Enter book title to return: ")

    for b in books:

        if b.title.lower() == title.lower():

            if not b.available:
                b.available = True
                print("Book returned successfuly.")
            else:
                print("Book was not borrowed.")

            return

    print("Book not found.")

# -----------------------------------------
# Show Library Info
# -----------------------------------------
def show_library_info():

    print("\n--- Library Info ---")
    print("Library Name:", library_info["name"])
    print("Total Books:", library_info["total_books"])

# -----------------------------------------
# Main Menu
# -----------------------------------------
def main():

    while True:

        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Show All Book")
        print("3. Search Book")
        print("4. Delet Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Library Info")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_all_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            borrow_book()

        elif choice == "6":
            return_book()

        elif choice == "7":
            show_library_info()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.") 



main()  






  