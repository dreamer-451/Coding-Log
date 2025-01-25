"""
HJ26 字符串排序

功能:
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。如，输入： By?e 输出： Be?y

数据范围：
输入的字符串长度满足 1 ≤ n ≤ 1000

输入：
输入字符串

输出：
输出字符串
"""

if __name__ == '__main__':
    strs = list(input())
    symbols = {}
    # 记住原字符串中各符号的位置
    for i in range(len(strs) - 1, -1, -1):
        if not strs[i].isalpha():
            symbols[i] = strs[i]
            strs.pop(i)
    # 对字符串中的字符进行排序，排序过程中忽略字符大小写的影响
    strs.sort(key=str.lower)
    keys = list(symbols.keys())
    keys.sort()
    for k in keys:
        strs.insert(k, symbols[k])
    strs = "".join(strs)
    print(strs)
