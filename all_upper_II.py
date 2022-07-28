# Проверить, есть ли в данной строке все символы в верхнем регистре.
# Если строка пуста или в ней нет ни одной буквы - функция должна вернуть False.
def is_all_upper(text: str) -> bool:
    return True if text.isupper() else False


if __name__ == "__main__":
    print("Example:")
    print(is_all_upper("ALL UPPER"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
