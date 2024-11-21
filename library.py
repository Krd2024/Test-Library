class Book:
    """
    Класс Book представляет книгу с уникальным идентификатором, названием, автором, годом издания и статусом доступности.

    Атрибуты класса:
        count (int): Счетчик для автоматического присвоения уникального ID каждой книге. Начинается с 1.
    """

    count = 1

    def __init__(self, title, author, year, status="в наличии"):
        self.id = Book.count
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        Book.count += 1

    def __str__(self):
        """
        Возвращает строковое представление аттрибутов объекта Book
        """
        return f"ID: {self.id}\nНазвание: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nСтатус: {self.status}\n"


class Library:
    books = []

    def add_book(self, title, author, year):

        book = Book(title, author, year)
        self.books.append(book)
        print(f"Книга '{title}' добавлена.\n")

    def delete_book(self, book_id):
        for book in self.books:

            if book.id == int(book_id):
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена.\n")
                return
        print(f"ОШИБКА! Книга ID: {book_id} не найдена.\n")

    def search_books(self, query):
        results = [
            book
            for book in self.books
            if query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query in book.year
        ]
        if results:
            print("Найдены книги:")
            for book in results:
                print(book)
        else:
            print("Книги по вашему запросу не найдены.\n")

    def display_books(self):
        if not self.books:
            print("В библиотеке нет книг.\n")
            return
        print("Список книг в библиотеке:")
        for book in self.books:
            print(book)

    def update_status(self, book_id, new_status):
        new_status = "в наличии" if new_status == 1 else "выдана"
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print(f"Статус книги '{book.title}' обновлен на '{new_status}'.\n")
                return
        print(f"ОШИБКА! Книга ID: {book_id} не найдена.\n")
