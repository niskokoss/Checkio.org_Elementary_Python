# Отсортируйте данный итератор таким образом, чтобы его элементы оказались в
# порядке убывания частоты их появления, то есть по количеству раз, которое они появляются в элементах.
# Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке, в котором стояли изначально в итераторе.


def frequency_sort(items):
    counts = {x: items.count(x) for x in items}
    sorted_counts = {k: counts[k] for k in sorted(counts.keys(), key=counts.get, reverse=True)}
    result = [x for x in sorted_counts for _ in range(sorted_counts[x])]
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
