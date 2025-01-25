"""
HJ42 学英语

具体规则如下:
1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
2.每三位数后记得带上计数单位 分别是thousand, million, billion.
3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and

说明：
数字为正整数，不考虑小数，转化结果为英文小写；
保证输入的数据合法
关键字提示：and，billion，million，thousand，hundred。

数据范围：
1 ≤ n ≤ 2000000

输入：
输入一个long型整数,数字为正整数，不考虑小数，转化结果为英文小写；保证输入的数据合法

输出：
输出相应的英文写法
"""

units = ["", "thousand", "million", "billion"]
bits_in_20 = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
ten_figures = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

if __name__ == '__main__':
    num = int(input())
    nums = []
    while num > 0:
        nums.append(num % 1000)
        num //= 1000
    ans = ""
    for i in range(len(nums)):
        num = int(nums[i])
        temp_ans = ""
        if num >= 100:
            temp = num // 100
            num %= 100
            temp_ans = f"{bits_in_20[temp]} hundred"
            if num > 0:
                temp_ans += " and "
        if num < 20:
            temp_ans += f"{bits_in_20[num]}"
            num = 0
        else:
            temp = num // 10
            num %= 10
            temp_ans += f"{ten_figures[temp]}"
        if num > 0:
            temp_ans += f" {bits_in_20[num]}"
        temp_ans += f" {units[i]} "
        ans = temp_ans + ans
    ans.strip()
    print(ans)
