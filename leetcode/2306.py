from itertools import permutations

def distinctNames(ideas):
    # 先将原有名称按首字母和单词后缀组成
    sufs = {}
    for idea in ideas:
        if idea[0] not in sufs:
            sufs[idea[0]] = {idea[1:]}
        else:
            sufs[idea[0]].add(idea[1:])
    # 从原称首字母库中任选两个组合，排除两首字母对应的共同单词后缀后随意组合
    n = 0
    for a, b in permutations(sufs, 2):
        temp_a = sufs[a].difference(sufs[b])
        temp_b = sufs[b].difference(sufs[a])
        n += len(temp_a) * len(temp_b)
    return n

if __name__ == '__main__':
    ideas = ["coffee","donuts","time","toffee"]
    print(distinctNames(ideas))
