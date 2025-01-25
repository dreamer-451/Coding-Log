def getRow(rowIndex):
    yh_tri = [[] for i in range(rowIndex + 1)]
    match rowIndex:
        case 0:
            yh_tri[0] = [1]
        case 1:
            yh_tri[1] = [1, 1]
        case _:
            yh_tri[1] = [1, 1]
            for i in range(2, rowIndex + 1):
                yh_tri[i].append(1)
                for j in range(i - 1):
                    yh_tri[i].append(yh_tri[i - 1][j] + yh_tri[i - 1][j + 1])
                yh_tri[i].append(1)
    return yh_tri[rowIndex]


if __name__ == '__main__':
    rowIndex0 = 0
    yhtri0 = getRow(rowIndex0)
    print(yhtri0)
    rowIndex1 = 1
    yhtri1 = getRow(rowIndex1)
    print(yhtri1)
    rowIndex2 = 2
    yhtri2 = getRow(rowIndex2)
    print(yhtri2)
    rowIndex3 = 3
    yhtri3 = getRow(rowIndex3)
    print(yhtri3)
    rowIndex5 = 5
    yhtri5 = getRow(rowIndex5)
    print(yhtri5)