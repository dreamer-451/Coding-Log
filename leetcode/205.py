def isIsomorphic(s, t):
    for i in range(len(s)):
        # 判断字符串中每个字符第一次出现的下标是否相等
        if s.index(s[i]) != t.index(t[i]):
            return False
    return True


if __name__ == '__main__':
    s = "paper"
    t = "title"
    ans = isIsomorphic(s, t)
    print(ans)