def fraction(cont):
    if len(cont) == 1:
        return [cont[0], 1]
    else:
        cont.reverse()
    n = 1
    m = cont[0]
    for i in range(1, len(cont)):
        n = cont[i] * m + n
        n, m = m, n
    n, m = m, n
    return [n, m]


if __name__ == '__main__':
    cont = [3, 2, 0, 2]
    print(fraction(cont))