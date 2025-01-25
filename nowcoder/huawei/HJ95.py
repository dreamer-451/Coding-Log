"""
HJ95 人民币转换

功能:
1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。
2、中文大写金额数字到“元”为止的，在“元”之后，应写“整"字，如532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写"整"字。
3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如6007.14，应写成“人民币陆仟零柒元壹角肆分“。
4、10应写作“拾”，100应写作“壹佰”。例如，1010.00应写作“人民币壹仟零拾元整”，110.00应写作“人民币壹佰拾元整”
5、十万以上的数字接千不用加“零”，例如，30105000.00应写作“人民币叁仟零拾万伍仟元整”

输入：
输入一个double数

输出：
输出人民币格式
"""
nums_10 = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾"]
flag = ["元", "万", "亿"]

if __name__ == '__main__':
    num0, num1 = input().split(".")
    nums0 = []
    num0 = int(num0)
    while num0 > 0:
        nums0.append(num0 % 10000)
        num0 //= 10000
    ans = ""
    for i in range(len(nums0)):
        n = nums0[i]
        temp_ans = ""
        if n > 1000:
            temp = n // 1000
            n %= 1000
            temp_ans += f"{nums_10[temp]}仟"
            if 0 < n < 100:
                temp_ans += "零"
        else:
            temp_ans += "零"
        if n > 100:
            temp = n // 100
            n %= 100
            temp_ans += f"{nums_10[temp]}佰"
            if 0 < n < 10:
                temp_ans += "零"
        if n > 10:
            temp = n // 10
            n %= 10
            if temp > 1:
                temp_ans += f"{nums_10[temp]}"
            temp_ans += "拾"
        if n > 0:
            temp_ans += f"{nums_10[n]}{flag[i]}"
        ans = temp_ans + ans
    if len(ans) != 0 and ans[0] == "零" and ans[1] != "元":
        ans = ans[1:]
    if int(num1) == 0:
        ans += "整"
    if int(num1[0]) != 0:
        ans += f"{nums_10[int(num1[0])]}角"
    if int(num1[1]) != 0:
        ans += f"{nums_10[int(num1[1])]}分"
    ans = "人民币" + ans
    print(ans)
