from library import Library
from check import is_digit


def main() -> None:
    """
    Основная функция управления библиотекой.
    Предоставляет следующие действия:

    - Добавление книги.
    - Удаление книги.
    - Поиск книги.
    - Просмотр всех книг.
    - Обновление статуса книги.
    - Завершение работы программы.
    """
    library = Library()

    while True:
        print("Меню упрвления библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Обновить статус книги")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")

            # Проверить поле заголовок на наличие символов
            if len(title.replace(" ", "")) > 0:
                author = input("Введите автора книги: ")

                # Проверить поле автор на наличие символов
                if len(author.replace(" ", "")) > 0:
                    year = input("Введите год издания книги: ")

                    # Функция is_digit(year) проверяет, состоит ли ввод для года только из цифр.
                    # Если год является числом, вызвать метоДобавления книги в библиотеку.
                    if is_digit(year):
                        library.add_book(title, author, year)
                    else:
                        print("-" * 25)
                        print("ОШИБКА! В поле 'year' используются только числа ")
                        print("-" * 25)
                else:
                    print("-" * 25)
                    print("ОШИБКА! Поле 'author' не может быть пустым")
                    print("-" * 25)
            else:
                print("-" * 25)
                print("ОШИБКА! Поле 'title' не может быть пустым")
                print("-" * 25)

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")

            # Функция is_digit(book_id) проверяет, состоит ли ввод для id книги только из цифр.
            # Если id является числом, вызвать метод удаления книги.
            if is_digit(book_id):
                library.delete_book(int(book_id))
            else:
                print("-" * 25)
                print("ОШИБКА! Только числа ")
                print("-" * 25)

        elif choice == "3":
            query = input("Введите название,автора или год для поиска: ")
            library.search_books(query)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = input("Введите ID книги: ")

            # Функция is_digit(book_id) проверяет, состоит ли ввод для id книги только из цифр.
            # Если это число, выбрать новый статус книги
            if is_digit(book_id):
                new_status = input("Hовый статус (1 - 'в наличии' или 0 - 'выдана'): ")

                # Если статус не в рамках предложенного, вывести ошибку.
                # Если статус в рамках предложенного,вызвать метод обновления статуса книги.
                if new_status != "1" and new_status != "0":
                    print("-" * 25)
                    print("Статус не определён")
                    print("-" * 25)
                else:
                    library.update_status(int(book_id), int(new_status))
            else:
                print("-" * 25)
                print("ОШИБКА! Только числа ")
                print("-" * 25)

        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("-" * 25)
            print("ОШИБКА! Неверный выбор. Попробуйте снова.\n")
            print("-" * 25)


main()
