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
        Возвращает строковое представление атрибутов объекта Book
        """
        return f"ID: {self.id}\nНазвание: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nСтатус: {self.status}\n"
