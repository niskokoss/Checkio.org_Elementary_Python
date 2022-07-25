# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.

def date_time(time: str) -> str:
    x = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
         7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    y = time.split(" ")
    date = y[0].split(".")
    time1 = y[1].split(":")
    if int(time1[1]) == 1 and int(time1[0]) == 1:
        result = f'{int(date[0])} {x[int(date[1])]} {int(date[2])} year {int(time1[0])} hour {int(time1[1])} minute'
    elif int(time1[1]) == 1:
        result = f'{int(date[0])} {x[int(date[1])]} {int(date[2])} year {int(time1[0])} hours {int(time1[1])} minute'
    elif int(time1[0]) == 1:
        result = f'{int(date[0])} {x[int(date[1])]} {int(date[2])} year {int(time1[0])} hour {int(time1[1])} minutes'
    else:
        result = f'{int(date[0])} {x[int(date[1])]} {int(date[2])} year {int(time1[0])} hours {int(time1[1])} minutes'
    return result


if __name__ == "__main__":
    print("Example:")
    print(date_time("09.07.1995 16:01"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
