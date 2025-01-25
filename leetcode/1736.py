def maximumTime(time):
    if time[1] < '4' or time[1] == '?':
        time = time[0].replace("?", "2") + time[1:]
    else:
        time = time[0].replace("?", "1") + time[1:]
    if time[0] == "2":
        time = time[0] + time[1].replace("?", "3") + time[2:]
    else:
        time = time[0] + time[1].replace("?", "9") + time[2:]
    time = time[:3] + time[3].replace("?", "5") + time[4]
    time = time[:4] + time[4].replace("?", "9")
    return time


if __name__ == '__main__':
    time = "??:??"
    format_time = maximumTime(time)
    print(format_time)