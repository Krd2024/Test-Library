# from library_class import Library


from library_class import Library


# def write_file(book: list = None, choice_action: str = "a") -> None:
#     with open("library_data.txt", choice_action, encoding="utf-8") as file:
#         if choice_action == "a":
#             file.write(
#                 f"{book.id},{book.title},{book.author},{book.year},{book.status}\n"
#             )
#         else:
#             library = Library()
#             for line in file:
#                 id, title, author, year, status = line.strip().split(",")
#                 # print(line.strip().split(","))
#                 # print(id, title, author, year, status)
#                 library.add_book(title, author, year, status)
