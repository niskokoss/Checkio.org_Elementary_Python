
# В этой миссии вам нужно создать функцию проверки пароля.
# 
# Это условия проверки:
# 
# длина должна быть больше 6;
# должен содержать хотя бы одну цифру, но не может состоять только из цифр;
# наличие цифр или просто цифр не применяется к паролю длиннее 9.
# строка ни в коем случае не должна содержать слово «пароль»;
# должен содержать не менее 3 разных букв (или цифр), даже если он длиннее 10
def is_acceptable_password(password: str):
    x = 0
    for i in password:
        if i.isdigit():
            x += 1
    if len(set(password)) < 3:
        return False
    elif "password" in password.lower():
        return False
    elif len(password) > 9:
        return True
    elif password.isdigit():
        return False
    elif len(password) >= 6 and x >= 1:
        return True
    else:
        return False

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
