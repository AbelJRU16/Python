from api_client import get_books, get_book, create_book, update_book, delete_book

def print_books(books):
    print("\nBooks:")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    print()

def main():
    while True:
        print("1. List all books")
        print("2. Get a book by ID")
        print("3. Add a new book")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            books = get_books()
            print_books(books)
        elif choice == '2':
            book_id = int(input("Enter book ID: "))
            book = get_book(book_id)
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
        elif choice == '3':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_id = int(input("Enter book ID: "))
            new_book = create_book({"id": book_id, "title": title, "author": author})
            print(f"Book added: {new_book}")
        elif choice == '4':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            updated_book = update_book(book_id, {"title": title, "author": author})
            print(f"Book updated: {updated_book}")
        elif choice == '5':
            book_id = int(input("Enter book ID to delete: "))
            response = delete_book(book_id)
            print(response)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
