def generate(numRows):
    yh_tri = [[] for i in range(numRows)]
    match numRows:
        case 1:
            yh_tri[0] = [1]
        case 2:
            yh_tri[0] = [1]
            yh_tri[1] = [1, 1]
        case _:
            yh_tri[0] = [1]
            yh_tri[1] = [1, 1]
            for i in range(2, numRows):
                yh_tri[i].append(1)
                for j in range(i - 1):
                    yh_tri[i].append(yh_tri[i - 1][j] + yh_tri[i - 1][j + 1])
                yh_tri[i].append(1)
    return yh_tri


if __name__ == '__main__':
    numRows1 = 1
    yh_tri1 = generate(numRows1)
    print(yh_tri1)
    numRows2 = 2
    yh_tri2 = generate(numRows2)
    print(yh_tri2)
    numRows3 = 3
    yh_tri3 = generate(numRows3)
    print(yh_tri3)
    numRows5 = 5
    yh_tri5 = generate(numRows5)
    print(yh_tri5)