from library import Library


def main():
    library = Library()

    def is_digit(string: str) -> bool:
        return string.replace(" ", "").isdigit()

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
            if len(title.replace(" ", "")) > 0:
                author = input("Введите автора книги: ")
                if len(author.replace(" ", "")) > 0:
                    year = input("Введите год издания книги: ")

                    # проверить данные ввода на соответствие
                    if is_digit(year):
                        library.add_book(title, author, year)
                    else:
                        print("-" * 25)
                        print(f"ОШИБКА! В поле {year} используются только числа ")
                        print("-" * 25)
                else:
                    print("-" * 25)
                    print(f"ОШИБКА! Поле {author} не может быть пустым")
                    print("-" * 25)
            else:
                print("-" * 25)
                print(f"ОШИБКА! Поле {title} не может быть пустым")
                print("-" * 25)

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")

            # Проверить является ли "book_id" цифрой
            if is_digit(book_id):
                library.delete_book(book_id)
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
            if is_digit(book_id):
                new_status = input("Hовый статус (1 - 'в наличии' или 0 - 'выдана'): ")
                if new_status != "1" and new_status != "0":
                    print("-" * 25)
                    print("Статус не определён")
                    print(type(new_status))
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
