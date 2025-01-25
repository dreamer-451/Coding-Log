"""
HJ103 Redraiment的走法

功能:
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。
他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？

数据范围：
每组数据长度满足 1 ≤ n ≤ 200，数据大小满足 1 ≤ val ≤ 350

输入：
数据共2行，第1行先输入数组的个数，第2行再输入梅花桩的高度

输出：
输出一个结果
"""

if __name__ == '__main__':
    n = int(input())
    highs = list(map(int, input().split()))
    step = []
    # 从第 i 个桩开始走
    for i in range(n):
        # 初始步数为 1
        step.append(1)
        # 走到第 i 个桩最多需要几步
        for j in range(i):
            # 查找 i 桩之前，是否有桩的高度低于第 i 桩，
            if highs[j] < highs[i]:
                # 走到第 i 桩的步数最多为当前走到 i 桩所需步数和走到 j 桩所需步数加一的最大值
                step[i] = max(step[i], step[j] + 1)
    print(max(step))
