import unittest
from library_class import Library


class TestMyLibrary(unittest.TestCase):
    @classmethod
    # def setUp(self):
    def setUpClass(cls):
        """Создание тествой библиотеки"""

        cls.library = Library()
        cls.library.add_book("Евгений Онегин", "Александр Пушкин", "1831")
        cls.library.add_book("Преступление и наказание", "Фёдор Достоевский", "1866")

    def test_book_titles(self):
        """Проверка, что добавленные книги присутствуют в библиотеке"""

        titles = [book.title for book in self.library.books]
        self.assertIn("Евгений Онегин", titles)
        self.assertIn("Преступление и наказание", titles)

    def test_book_search(self):
        """
        Тестирует поиск книги по автору, названию и году издания.

        Проверяется, что при поиске по автору, названию и году издания
        соответствующая книга может быть найдена в библиотеке.
        """

        test_author = "Пушкин"
        test_title = "Онегин"
        test_yaer = "1831"

        # Вызывается метод поиска по автору с дополнительным параметром
        # test=True, который укажет методу вернуть список
        found_books = self.library.search_books(test_author, test=True)

        # Проверяет, что найдена хотя бы одна книга
        self.assertTrue(len(found_books) > 0, "Книга не найдена по автору")

        # Проверяет, что найденная книга соответствует ожидаемому автору
        self.assertEqual(
            found_books[0].author,
            "Александр Пушкин",
            "Найдена книга неправильного автора",
        )

        # Вызывается метод поиска по названию книги с дополнительным параметром
        # test=True, который укажет методу вернуть список
        found_books = self.library.search_books(test_title, test=True)

        # Проверяет, что найдена хотя бы одна книга
        self.assertTrue(len(found_books) > 0, "Книга не найдена по названию")

        # Проверяет, что найденная книга соответствует ожидаемому названию
        self.assertEqual(
            found_books[0].title,
            "Евгений Онегин",
            "Найдена книга с неправильным названием",
        )

        # Вызывается метод поиска по году издания с дополнительным параметром
        # test=True, который укажет методу вернуть список
        found_book = self.library.search_books(test_yaer, test=True)

        # Проверяет, что найденный год издания книги соответствует ожидаемому
        self.assertEqual(
            found_book[0].year, test_yaer, "Найдена книга с другим годом издания"
        )

    def test_update_status(self):
        """
        Тестирует обновление статуса книги в библиотеке.

        Проверяется, что статус книги обновляется корректно.
        В данном случае обновляется статус книги с id=2 на 'выдана' (status=0).
        """

        test_id = 2
        test_new_status = 0  # "выдана"

        # Вызывает метод обновления статуса книги
        # Передаёт ID книги и статус который установить
        self.library.update_status(test_id, test_new_status)

        # Получает книгу по ID
        book = [book for book in self.library.books if book.id == test_id][0]

        # Сравнить статус с переданным при вызове метода
        self.assertEqual(book.status, "выдана", "Статус не изменился")


class TestDeleteBook(unittest.TestCase):

    def setUp(self):
        """Создание тествой библиотеки"""

        self.library = Library()
        self.library.add_book("Евгений Онегин", "Александр Пушкин", "1831")
        self.library.add_book("Преступление и наказание", "Фёдор Достоевский", "1866")

    def test_book_delete(self):
        """
        1.Тест на удаление книги.Задаёт ID книги равный 1,
          находит книгу в списке и удаляет.
          Повторный поиск книги по ID должен дать пустой список.

        2.Сравнивается длина списка до удаления и после.
          После удаления длина списка должна уменьшиться
          на один элемент

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


unittest.main()
