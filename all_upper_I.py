# Проверить все ли символы в строке являются заглавными.
# Если строка пустая или в ней нет букв - функция должна вернуть True.

def is_all_upper(text: str) -> bool:
    x = text.replace(" ", "")
    return True if x.isupper() == True or len(x) == 0 or x.isdecimal() else False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
