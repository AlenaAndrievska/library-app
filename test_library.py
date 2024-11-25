import unittest
from services import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")
        self.assertEqual(self.library.books[0].author, "George Orwell")
        self.assertEqual(self.library.books[0].year, 1949)
        self.assertEqual(self.library.books[0].status, "в наличии")

    def test_add_book_invalid_year(self):
        self.library.add_book("1984", "George Orwell", "invalid_year")
        self.assertEqual(len(self.library.books), 0)

    def test_add_book_empty_fields(self):
        self.library.add_book("", "George Orwell", "1949")
        self.assertEqual(len(self.library.books), 0)

    def test_remove_book(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_book_not_found(self):
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books_by_title(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.library.add_book("Animal Farm", "George Orwell", "1945")
        self.library.search_books("1984")
        self.assertEqual(len(self.library.books), 2)

    def test_search_books_by_author(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.library.add_book("Animal Farm", "George Orwell", "1945")
        self.library.search_books("Orwell")
        self.assertEqual(len(self.library.books), 2)

    def test_search_books_by_year(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.library.add_book("Animal Farm", "George Orwell", "1945")
        self.library.search_books("1949")
        self.assertEqual(len(self.library.books), 2)

    def test_change_book_status(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.library.change_book_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_change_book_status_invalid(self):
        self.library.add_book("1984", "George Orwell", "1949")
        self.library.change_book_status(1, "invalid_status")
        self.assertEqual(self.library.books[0].status, "в наличии")

if __name__ == "__main__":
    unittest.main()
