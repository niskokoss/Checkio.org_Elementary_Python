# Попробуйте выяснить какое количество нулей содержит данное число в конце.
#
# Ваша миссия здесь — создать функцию, которая получает кортеж и возвращает кортеж
# с 3 элементами — первым, третьим и вторым элементом из последнего для данного массива.


def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
