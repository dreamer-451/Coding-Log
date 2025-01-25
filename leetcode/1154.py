def dayOfYear(date):
    dayOfMonth = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    if year % 4 == 0 and year % 100 != 0:
        isLeap = 1
    elif year % 400 == 0:
        isLeap = 1
    else:
        isLeap = 0
    if month >= 3 and isLeap == 1:
        days = 1
    else:
        days = 0
    for i in range(1, month):
        days += dayOfMonth[i]
    days += day
    return days


if __name__ == '__main__':
    date = "2004-03-01"
    days = dayOfYear(date)
    print(days)