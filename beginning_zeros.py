# Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.


def beginning_zeros(number: str) -> int:
    x = list(map(int, str(number)))
    z = 0
    for i in range(len(x)):
        if x[0] == 0:
            z += 1
            del x[0]
        else:
            break
    return z


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
