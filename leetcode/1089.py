def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    l = len(arr)
    while i < l:
        try:
            i += arr[i:].index(0)
        except ValueError:
            break
        else:
            arr.insert(i, 0)
            i += 2
            arr.pop()


if __name__ == '__main__':
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicateZeros(arr)
    print(arr)