"""
HJ6 质数因子

功能:
输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围：
1 ≤ n ≤ 2×10^8+14

输入：
输入一个整数

输出：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
"""
import math

if __name__ == '__main__':
    n = int(input())
    m = int(math.sqrt(n)) + 1
    ans = []
    i = 2
    while i < m:
        if n % i == 0:
            ans.append(i)
            n //= i
        else:
            i += 1
    if n >= 2:
        ans.append(n)
    for a in ans:
        print(a, end=' ')
