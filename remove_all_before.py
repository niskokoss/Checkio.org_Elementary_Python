# Не все элементы важны. Вам нужно удалить из списка все элементы до указанного.
# Есть два нюанса: (1) если в списке нет элемента до которого нужно удалить остальные элементы
# , то список не должен измениться. (2) если list пустой, то он должен остаться пустым.
# Входные данные: Список и элемент до которого нужно удалить другие элементы.
# Выходные данные: Набор значений (кортеж, список, итератор ...).


from typing import Iterable


def remove_all_before(items: list, border: int):
    if border in items:
        for i in range(len(items)):
            if i == border:
                while True:
                    if items[0] != border:
                        items.pop(0)
                    else:
                        return items
        return items
    else:
        return items



if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
