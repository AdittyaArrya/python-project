# Task 4: Menu-Driven Command Line Interface

from inventory import LibraryInventory
from book import Book

def menu():
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search by Title")
    print("6. Search by ISBN")
    print("0. Exit")

def main():
    inv = LibraryInventory()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")

                book = Book(title, author, isbn)
                inv.add_book(book)
                print("Book added.")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inv.search_by_isbn(isbn)
                if book:
                    book.issue()
                    print("Book issued.")
                else:
                    print("Book not found.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inv.search_by_isbn(isbn)
                if book:
                    book.return_book()
                    print("Book returned.")
                else:
                    print("Book not found.")

            elif choice == "4":
                inv.display_all()

            elif choice == "5":
                title = input("Enter title: ")
                results = inv.search_by_title(title)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")

            elif choice == "6":
                isbn = input("Enter ISBN: ")
                book = inv.search_by_isbn(isbn)
                if book:
                    print(book)
                else:
                    print("Book not found.")

            elif choice == "0":
                inv.save()
                print("Saving and exiting...")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
