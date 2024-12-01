from book import Book


def write_read_file(books: list = None, choice_action: str = "w") -> None:
    """
    Функция для записи или чтения данных о книгах в/из файла `library_data.txt`.

    Args:
        books (list, optional): Список объектов книг.
        choice_action (str, optional): Режим работы с файлом.


    Функциональность:
        - Если `choice_action` равно "w", функция записывает информацию о книгах из списка `books` в файл `library_data.txt` в формате CSV (id, title, author, year, status).
        - Если `choice_action` отличается от "w", функция читает строки из файла, обрабатывает их и добавляет книги в объект библиотеки.

    Исключения:
        - При чтении файла: если строка в файле не соответствует ожидаемому формату, выводится сообщение "Нет записи".

    """
    # Создаем объект библиотеки
    library = Library()

    with open("library_data.csv", choice_action, encoding="utf-8") as file:

        # Перезаписывает файл если режим "w
        # Записывает новую коллекцию с именёнными или удаленными объектами книг
        if choice_action == "w":
            for book in books:
                file.write(
                    f"{book.id},{book.title},{book.author},{book.year},{book.status}\n"
                )
        else:
            try:
                for line in file:

                    # Удаление лишних пробелов и символов новой строки,
                    # Присвоение значений переменным
                    id, title, author, year, status = line.strip().split(",")
                    # print(line.strip().split(","))

                    # Вызов метода добавления книги в список библиотеки
                    # Получает данные из файла
                    library.add_book(title, author, year, status)

            # Вызов метода записи в файл списка книг библиотеки.
            # Этот метод перезапишет файл с данными о книгах, начиная с нового ID для каждой книги.
            # Если необходимо, раскомментируйте строку.
            # library.write_file()
            except ValueError:
                print("Нет записи")


class Library:
    # Список книг в библиотеке
    books = []

    def add_book(self, title: str, author: str, year: str, status: str = "в наличии"):
        """
        Создает новый объект книги (Book) с переданными параметрами
        и добавляет его в список книг библиотеки (self.books).
        """
        # Создание нового объекта книги
        book = Book(title, author, year, status)

        # Добавление книги в список
        self.books.append(book)
        print(f"Книга '{title}' добавлена.\n")

        # Вызов метода записи в файл
        # Для обновления данных после добавления книги
        self.write_file()

    def write_file(self):
        """
        Вызывает функцию `write_file`, передавая ей список всех книг,
        хранящихся в библиотеке (self.books) для записи данных в файл (формат CSV).
        """
        write_read_file(self.books)

    def delete_book(self, book_id: int) -> None:
        """
        Ищет книгу с указанным ID в библиотеке.
        Если книга найдена, она удаляется. Если книга с таким ID отсутствует,
        выводится сообщение об ошибке.

        Args:
            book_id(int): ID книги
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена.\n")

                # Вызывает метод записи в файл
                # Для обновления данных после удаления
                self.write_file()

                return
        print(f"ОШИБКА! Книга ID: {book_id} не найдена.\n")

    def search_books(self, query: str, test: bool = False) -> None:
        """
        Ищет книги по названию,автору и ID в библиотеке.
        Найденные книги выводит в терминал.
        Поиск производится в нижнем регистре.
        Если книги не найдены, выводмится сообщение о том,что книги не найдены.

        Args:
            query(str): Название книги, автор или год издания.
            test(bool): Если True, метод возвращает результат поиска как список.
                        По умолчанию False.
        """
        # список который содержит книги, соответствующие поисковому запросу query
        results = [
            book
            for book in self.books
            if query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query in book.year
        ]
        # Если метод вызван из теста, вернёт результат поиска в виде списка
        if test:
            return results

        # Если есть что показать,то покажет
        if results:
            print("-" * 40)
            print("Найдены книги:\n")
            for book in results:
                print(book)
            print("Нажмите Enter для продолжения.")
            input()
        else:
            print("Книги по вашему запросу не найдены.\n")

    def display_books(self) -> None:
        """
        Перебирает все книги, хранящиеся в коллекции библиотеки, и выводит информацию
        о каждой книге. Если библиотека пуста, выводится сообщение о том, что книги отсутствуют.
        """

        if not self.books:
            print("В библиотеке нет книг.\n")
            return
        print("Список книг в библиотеке:")
        print("-" * 40)
        for book in self.books:
            print(book)
        print("Нажмите Enter для продолжения.")
        input()

    def update_status(self, book_id: int, new_status: int) -> None:
        """
        Статус может быть либо "в наличии", либо "выдана". Если книга с таким ID
        не найдена, выводится сообщение об ошибке.

        Args:
            book_id (int): Идентификатор книги, чей статус необходимо обновить.
            new_status (int): Новый статус книги. Может быть "в наличии" если new_status == 1
            или "выдана" если new_status == 0
        """

        new_status = "в наличии" if new_status == 1 else "выдана"

        # Поиск книги по ID и присвоение нового статуса
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print(f"Статус книги '{book.title}' обновлен на '{new_status}'.\n")

                # Вызов метода записи в файл
                # Для обновления данных после изменения статуса
                self.write_file()

                return
        print(f"ОШИБКА! Книга ID: {book_id} не найдена.\n")
