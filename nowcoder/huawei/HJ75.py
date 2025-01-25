"""
HJ75 公共子串计算

功能:
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
进阶：时间复杂度：O(n^3)，空间复杂度：O(n)

数据范围：
字符串长度：1 ≤ s ≤ 150

输入：
输入两个只包含小写字母的字符串

输出：
输出一个整数，代表最大公共子串的长度

示例：
str1 = "12456"
str2 = "1a23b456c"
初始化：
maxlen=0
进循环后：
maxlen=0    i=0    str1[i-0:i+1]=str1[i:i+1]=str1[i]=str1[0]="1"    maxlen=1
maxlen=1    i=1    str1[i-1:i+1]=str1[0:2]="12"    maxlen=1
maxlen=1    i=2    str1[i-1:i+1]=str1[1:3]="24"    maxlen=1
maxlen=1    i=3    str1[i-1:i+1]=str1[2:4]="45"    maxlen=2
maxlen=2    i=4    str1[i-2:i+1]=str1[2:5]="456"   maxlen=3
退出循环：
maxlen=3
"""

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    # 最大公共子串长度，初始值为0
    maxlen = 0
    for i in range(len(str1)):
        #查找str1中的字符是否在str2中，若是往后扩展一位，若否则往后滑动一位
        if str1[i - maxlen: i + 1] in str2:
            maxlen += 1
    print(maxlen)
