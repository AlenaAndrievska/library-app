from typing import List


class Book:
    """
    Класс, представляющий книгу.

    :param int book_id: Уникальный идентификатор книги.
    :param str title: Название книги.
    :param str author: Автор книги.
    :param int year: Год издания книги.
    :param str status: Статус книги ("в наличии" или "выдана").
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :returns: Строковое представление книги.
        :rtype: str
        """
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"

class Library:
    """
    Класс, представляющий библиотеку книг.

    :param list books: Список книг в библиотеке.
    :param int next_id: Следующий уникальный идентификатор для новой книги.
    """
    def __init__(self):
        self.books: List[Book] = []
        self.next_id: int = 1

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавляет новую книгу в библиотеку.

        :param str title: Название книги.
        :param str author: Автор книги.
        :param str year: Год издания книги.

        :return None
        """
        if not title or not author or not year:
            print("All fields must be filled.")
            return

        try:
            year = int(year)
        except ValueError:
            print("Year must be a number.")
            return

        book = Book(self.next_id, title, author, year)
        self.books.append(book)
        self.next_id += 1
        print(f"Book added: {book}")

    def remove_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по её идентификатору.

        :param int book_id: Идентификатор книги.

        :return None
        """
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print(f"Book with ID {book_id} not found.")

    def search_books(self, keyword: str) -> None:
        """
        Ищет книги по ключевому слову в названии, авторе или году.

        :param str keyword: Ключевое слово для поиска.

        :return None
        """
        try:
            year = int(keyword)
            results = [book for book in self.books if book.year == year]
        except ValueError:
            results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def display_books(self) -> None:
        """
        Отображает все книги в библиотеке.

        :return None
        """
        if self.books:
            print("Library books:")
            for book in self.books:
                print(book)
        else:
            print("The library is empty.")

    def change_book_status(self, book_id: int, new_status: str) -> None:
        """
        Изменяет статус книги по её идентификатору.

        :param int book_id: Идентификатор книги.
        :param str new_status: Новый статус книги ("в наличии" или "выдана").

        :return None
        """
        valid_statuses = ["в наличии", "выдана"]
        if new_status not in valid_statuses:
            print(f"Invalid status. Please enter 'в наличии' or 'выдана'.")
            return

        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                print(f"Book status updated: {book}")
                return
        print(f"Book with ID {book_id} not found.")