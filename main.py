from services import Library

def main() -> None:
    """
    Основная функция для управления библиотекой книг.

    :return None
    """
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Change Book Status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Enter book ID to remove: "))
            library.remove_book(book_id)
        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            library.search_books(keyword)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Enter book ID to change status: "))
            new_status = input("Enter new status ('в наличии' or 'выдана'): ")
            library.change_book_status(book_id, new_status)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




