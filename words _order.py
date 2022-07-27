# У вас есть текст и список слов.
# Вам нужно проверить, появляются ли слова в списке в том же порядке, что и в данном тексте.
# 
# Случаи, которые вы должны ожидать при решении этой задачи:
# 
# слово из списка отсутствует в тексте — ваша функция должна вернуть False;
# любое слово может встречаться в тексте более одного раза — используйте только первое;
# два слова в данном списке совпадают - ваша функция должна вернуть False;
# условие чувствительно к регистру, что означает, что «привет» и «привет» — это два разных слова;
# текст включает только английские буквы и пробелы.
def words_order(text: str, words: list) -> bool:
    if len(words) != len(list(set(words))):
        return False
    text = text.split(" ")
    x = []
    for i in words:
        if i in text:
            for t in text:
                if t == i:
                    if text.index(t) not in x:
                        x.append(text.index(t))
        else:
            return False
    if len(x) > len(words):
        return False
    return True if x == sorted(set(x)) else False


if __name__ == "__main__":
    print("Example:")
    print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
