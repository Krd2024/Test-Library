import unittest
from library_class import Library
from book import Book


class TestMyLibrary(unittest.TestCase):
    library = Library()

    def setUp(self):
        """Создание тествой библиотеки"""

        self.library.add_book("Война и мир", "Лев Толстой", "1869")
        self.library.add_book("Преступление и наказание", "Фёдор Достоевский", "1866")

    def test_book_titles(self):
        """Проверка, что добавленные книги присутствуют в библиотеке"""

        titles = [book.title for book in self.library.books]
        self.assertIn("Война и мир", titles)
        self.assertIn("Преступление и наказание", titles)

    def test_book_delete(self):
        """
        Тест на удаление книги.Задаёт ID книги равный 1,
        находит книгу в списке и удаляет.
        Повторный поиск книги по ID должен дать пустой список,
        что проверяется.
        Сравнивается длина списка до удаления и после

        """
        # Задать ID книге
        book_id = 1
        # Начальная длина списка
        count = len(self.library.books)
        # Поиск книги
        book = [book for book in self.library.books if book.id == book_id]
        # Вызывается метод удаления
        self.library.delete_book(book_id)
        # Поиск книги
        book = [book for book in self.library.books if book.id == book_id]
        # Проверка поиска книги после удаления
        self.assertEqual(len(book), 0, "Книга не была удалена")
        # Проверка равенства общей длины списка до и после удаления книги
        self.assertEqual(
            count - 1, len(self.library.books), "Удалено больше одной книги"
        )

    def test_book_search(self):
        pass


unittest.main()
