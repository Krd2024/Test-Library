def is_digit(string: str) -> bool:
    """
    Проверяет, состоит ли строка только из цифр
    после удаления всех пробелов.

    """
    return string.replace(" ", "").isdigit()
