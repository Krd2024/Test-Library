from book import Book


class Library:
    books = []

    def add_book(self, title, author, year):

        book = Book(title, author, year)
        self.books.append(book)
        print(f"Книга '{title}' добавлена.\n")

    def delete_book(self, book_id: int) -> None:
        """
        Ищет книгу с указанным ID в библиотеки.
        Если книга найдена, она удаляется. Если книга с таким ID отсутствует,
        выводится сообщение об ошибке.
        """
        for book in self.books:

            if book.id == book_id:
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена.\n")
                return
        print(f"ОШИБКА! Книга ID: {book_id} не найдена.\n")

    def search_books(self, query: str) -> None:
        """
        Ищет книги по названию,автору и ID в библиотеке.
        Найденные книги выводит в терминал.
        Поиск производится в нижнем регистре.
        Если книги не найдены, выводмится сообщение о том,что книги не найдены.

        Args:
            query(str): Название книги, автор или год издания.
        """
        results = [
            book
            for book in self.books
            if query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query in book.year
        ]
        if results:
            print("-" * 25)
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
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print(f"Статус книги '{book.title}' обновлен на '{new_status}'.\n")
                return
        print(f"ОШИБКА! Книга ID: {book_id} не найдена.\n")
