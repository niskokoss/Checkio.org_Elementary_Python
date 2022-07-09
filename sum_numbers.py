# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
# Если число является частью слова, то его суммировать не нужно.

def sum_numbers(text: str) -> int:
    t = 0
    for i in text.split():
        if i.isnumeric():
            t += int(i)
    return t


if __name__ == "__main__":
    print("Example:")
    print(sum_numbers("hi"))


    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
