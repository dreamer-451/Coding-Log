def beautifulIndices(s, a, b, k):
    ans = []
    if a not in s or b not in s:
        return ans
    index_a = []
    index_b = []
    i = s.find(a)
    j = 0
    while i != -1:
        index_a.append(j + i)
        j += i + 1
        i = s[j:].find(a)
    i = s.find(b)
    j = 0
    while i != -1:
        index_b.append(j + i)
        j += i + 1
        i = s[j:].find(b)
    for i in range(len(index_a)):
        for j in range(len(index_b)):
            if abs(index_b[j] - index_a[i]) <= k:
                ans.append(index_a[i])
                break
    return ans


if __name__ == '__main__':
    s = "isawsquirrelnearmysquirrelhouseohmy"
    a = "my"
    b = "squirrel"
    k = 15
    ans = beautifulIndices(s, a, b, k)
    print(ans)