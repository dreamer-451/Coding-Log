"""
HJ22 汽水瓶

功能:
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。

数据范围：
输入的正整数满足 1 ≤ n ≤ 100

输入：
输入文件最多包含 10 组测试数据。
每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。
n=0 表示输入结束，你的程序不应当处理这一行。

输出：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
"""
import sys

'''
模拟法：
模拟汽水瓶交换规则进行计算
'''
def simulate(empty_bottles):
    bottles = 0
    while empty_bottles != 0 and empty_bottles != 1:
        if empty_bottles % 3 == 0:
            temp = empty_bottles // 3
            bottles += temp
            empty_bottles = temp
        elif empty_bottles % 3 == 1:
            temp = empty_bottles // 3
            bottles += temp
            empty_bottles = temp + 1
        elif empty_bottles % 3 == 2:
            temp = empty_bottles // 3
            bottles += temp + 1
            empty_bottles = temp
    return bottles

'''
数学逻辑推理法：
三个空瓶换一瓶饮料，可以借空瓶，但需要还对应的空瓶，即借n瓶还n瓶。
故而，因为换到的饮料只有一瓶，所以最多只能借一瓶，
所以，推理可知，至少需要2个空瓶便可以喝到一瓶饮料，
即 2<初始空瓶数> + (1)<所借空瓶数> - 3<交换所需空瓶数> + 1<交换所得瓶数> - (1)<返还所借空瓶数> = 0
'''
def infer(empty_bottles):
    bottles = empty_bottles // 2
    return bottles

if __name__ == '__main__':
    for line in sys.stdin:
        empty_bottles = int(line)
        if empty_bottles == 0:
            break
        #bottles = simulate(empty_bottles)
        bottles = infer(empty_bottles)
        print(bottles)
