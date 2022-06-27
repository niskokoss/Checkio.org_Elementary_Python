# У вас есть последовательность строк, и вы хотите определить наиболее часто встречающуюся строку в последовательности. Он может быть только один.
#
# Вход: непустой список строк.
#
# Выход: строка.


def most_frequent(data: list) -> str:
    return max(data, key=lambda a: data.count(a))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
