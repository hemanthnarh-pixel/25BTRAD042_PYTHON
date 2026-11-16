class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")


books = []

while True:
    print("\n--- LIBRARY MANAGEMENT ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        books.append(Book(title, author))
        print("Book added successfully.")

    elif choice == "2":
        title = input("Enter title to issue: ")
        found = False

        for book in books:
            if book.title.lower() == title.lower():
                book.issue()
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "3":
        title = input("Enter title to return: ")
        found = False

        for book in books:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        if not books:
            print("No books available.")

        for book in books:
            book.display()
            print("---------------")

    elif choice == "5":
        print("Exiting library system.")
        break

    else:
        print("Invalid choice.")