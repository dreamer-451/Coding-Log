def countPrimes(n):
    if n <= 1:
        return 0
    primeNum = [0, 0] + [1] * (n - 2)
    # 任何一个大于1的数，它的倍数均非质数
    for i in range(2, n):
        if i * i < n:
            for j in range(i * i, n, i):
                primeNum[j] = 0
    return sum(primeNum)


if __name__ == '__main__':
    n = 5000000
    print(countPrimes(n))