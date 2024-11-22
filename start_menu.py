from library_class import Library, write_read_file
from check import is_digit

# from write_read import write_file


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
    write_read_file(choice_action="r")

    while True:
        print("Меню упрвления библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Обновить статус книги")
        print("0. Выход")
        print("-" * 40)
        choice = input("Выберите действие: ")
        print()

        # Ввести данные для новой книги (заголовок,автор,год издания)
        if choice == "1":
            # Заголов для книги
            title = input("Введите название книги: ")

            # Проверить поле заголовок на наличие символов
            if len(title.replace(" ", "")) > 0:

                # Имя автора книги
                author = input("Введите автора книги: ")

                # Проверить поле автор на наличие символов
                if len(author.replace(" ", "")) > 0:

                    # Год издания книги
                    year = input("Введите год издания книги: ")

                    # Функция is_digit(year) проверяет, состоит ли ввод для года только из цифр.
                    # Если год является числом, вызвать метоДобавления книги в библиотеку.
                    if is_digit(year):
                        library.add_book(title, author, year)
                        library.write_file()
                    else:
                        print("-" * 40)
                        print("ОШИБКА! В поле 'year' используются только числа ")
                        print("-" * 40)
                else:
                    print("-" * 40)
                    print("ОШИБКА! Поле 'author' не может быть пустым")
                    print("-" * 40)
            else:
                print("-" * 40)
                print("ОШИБКА! Поле 'title' не может быть пустым")
                print("-" * 40)
        # Удаление книги по ID
        elif choice == "2":

            # ID книги
            book_id = input("Введите ID книги для удаления: ")

            # Функция is_digit(book_id) проверяет, состоит ли ввод для id книги только из цифр.
            # Если id является числом, вызвать метод удаления книги.
            if is_digit(book_id):
                library.delete_book(int(book_id))
                library.write_file()
            else:
                print("-" * 40)
                print("ОШИБКА! Только числа ")
                print("-" * 40)

        # Поиск книги по названию,автору или году издания
        elif choice == "3":

            query = input("Введите название,автора или год для поиска: ")

            # Проверить ввод на наличие символов
            if len(query.replace(" ", "")) > 0:

                # Вызов метода поиска книги
                library.search_books(query)
            else:
                print("-" * 40)
                print("ОШИБКА! Поиск не может быть пустым")
                print("-" * 40)

        # Показать все книги
        elif choice == "4":
            library.display_books()

        # Обновить статус книги
        # Поиск производится по ID
        elif choice == "5":

            # получить ID книги
            book_id = input("Введите ID книги: ")

            # Функция is_digit(book_id) проверяет, состоит ли ввод для id книги только из цифр.
            # Если это число, выбрать новый статус книги
            if is_digit(book_id):
                new_status = input("Hовый статус (1 - 'в наличии' или 0 - 'выдана'): ")

                # Если статус не в рамках предложенного, вывести ошибку.
                # Если статус в рамках предложенного,вызвать метод обновления статуса книги.
                if new_status != "1" and new_status != "0":
                    print("-" * 40)
                    print("Статус не определён")
                    print("-" * 40)
                else:
                    # Вызоа метода обновления статуса
                    library.update_status(int(book_id), int(new_status))

                    # Вызов метода записи в файл
                    # Для обновления данных после изменения статуса
                    library.write_file()
            else:
                print("-" * 40)
                print("ОШИБКА! Только числа ")
                print("-" * 40)

        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("-" * 40)
            print("ОШИБКА! Неверный выбор. Попробуйте снова.\n")
            print("-" * 40)


main()
