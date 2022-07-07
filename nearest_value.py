# Найдите ближайшее значение к переданному.
# 
# Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
# 
# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. 
# И нам нужно найти ближайшее значение к цифре 9.
# Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7,
# а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.


def nearest_value(values: set, one: int) -> int:
    a = 999999999999
    for i in values:
        if i == one:
            return i
        if abs(i - one) < abs(a - one):
            a = i
    return a


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
