"""
HJ41 称砝码

功能:
现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。
现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
注：称重重量包括 0

数据范围：
每组输入数据满足 1 ≤ n ≤ 10，1 ≤ mi ≤ 2000，1 ≤ xi ≤ 10

输入：
对于每组测试数据：
第一行：n --- 砝码的种数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])

输出：
利用给定的砝码可以称出的不同的重量数
"""

if __name__ == '__main__':
    n = int(input())
    m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    weights = {0}
    # 遍历砝码种类
    for i in range(n):
        # 对每种砝码，遍历该种砝码数量
        for j in range(x[i]):
            temp = []
            # 每增加一个砝码，增加的可称重重量相当于原有的可称重重量加上该砝码的种类
            for weight in weights:
                temp.append(weight + m[i])
            # 将增加的重量种类增添进可称重重量集合中，通过集合去重
            weights.update(temp)
    print(len(weights))
