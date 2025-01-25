def relativeSortArray(arr1, arr2):
    start = 0
    for a2 in arr2:
        n = arr1.count(a2)
        for i in range(start, start + n):
            ind = arr1.index(a2, i)
            if i == ind:
                continue
            a1 = arr1[i]
            arr1[i] = a2
            arr1[ind] = a1
        start += n
    arr1[start:] = sorted(arr1[start:])
    return arr1


if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    relativeSortArray(arr1, arr2)
    print(arr1)
    ar1 = [28,6,22,8,44,17]
    ar2 = [22,28,8,6]
    relativeSortArray(ar1, ar2)
    print(ar1)