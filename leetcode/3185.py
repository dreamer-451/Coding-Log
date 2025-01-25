# 方法一：模拟法，先统计时间序列，根据序列下标一一对比
def countCompleteDayPairs_sim(hours):
    hs = {}
    for i in range(24):
        hs[i] = []
    for i in range(len(hours)):
        hs[hours[i] % 24].append(i)
    l0, l12 = len(hs[0]), len(hs[12])
    pairs = (l0 - 1) * l0 // 2 + (l12 - 1) * l12 // 2
    for h in list(range(1, 12)) + list(range(13, 24)):
        k = 0
        for i in range(len(hs[h])):
            for j in range(k, len(hs[24 - h])):
                if hs[24 - h][j] > hs[h][i]:
                    pairs += len(hs[24 - h][j:])
                    k = j
                    break
    return pairs

# 方法二：
# 循环时间序列，每个时间点，对应的可组时间对数为该点左边可组合时间点数
def countCompleteDayPairs(hours):
    hs = [0] * 24
    pairs = 0
    for hour in hours:
        pairs += hs[(24 - hour % 24) % 24]
        hs[hour % 24] += 1
    return pairs

if __name__ == '__main__':
    hours = [12,18,29,19,27,5]
    print(countCompleteDayPairs_sim(hours))
    print(countCompleteDayPairs(hours))
