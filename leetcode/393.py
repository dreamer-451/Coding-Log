def validUtf8(data):
    bin_data = [bin(d).replace("0b", "") for d in data]
    l = len(data)
    for i in range(l):
        l1 = len(bin_data[i])
        if l1 < 8:
            bin_data[i] = "0" * (8 - l1) + bin_data[i]
    i = 0
    while i < l:
        if "0" not in bin_data[i]:
            return False
        ind = bin_data[i].index("0")
        if ind == 1 or ind > 4:
            return False
        elif ind == 0:
            i += 1
        else:
            if i + int(ind) - 1 >= l:
                return False
            for j in range(i + 1, i + int(ind)):
                if bin_data[j][:2] != "10":
                    return False
            i += int(ind)
    return True


if __name__ == '__main__':
    data = [197, 130, 1]
    ans = validUtf8(data)
    print(ans)