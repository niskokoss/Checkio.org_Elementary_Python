# В этой миссии вам нужно создать функцию проверки пароля.
# 
# Это условия проверки:
# 
# длина должна быть больше 6;
# должен содержать хотя бы одну цифру.
def is_acceptable_password(password: str):
    x = 0
    for i in password:
        if i.isdigit():
            x += 1
    return True if len(password) >= 6 and x >= 1 else False



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
