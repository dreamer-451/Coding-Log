"""
HJ61 放苹果

功能:
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。

数据范围：
0 ≤ m ≤ 10，1 ≤ n ≤ 10

输入：
输入两个int整数

输出：
输出结果，int型
"""

# 苹果数为m，盘子数为n
def apple(m, n):
    # 只有1个苹果或盘子时，放法只有一种
    if m == 0 or m == 1 or n == 1:
        return 1
    # 若苹果数少于盘子数，则放置方法与将m个苹果放在m个盘子的方法数一致
    elif m < n:
        return apple(m, m)
    # 剩余多个苹果或盘子的情况：
    # 1、一个盘子不放苹果，即apple(m, n - 1)
    # 2、每个盘子至少放一个苹果，即apple(m - n, n)
    else:
        return apple(m, n - 1) + apple(m - n, n)

if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    num = apple(m, n)
    print(num)
