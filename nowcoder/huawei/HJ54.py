"""
HJ54 表达式求值

功能:
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。

数据范围：
运算过程中和最终结果均满足 ∣val∣ ≤ 2^31−1  ,即只进行整型运算，确保输入的表达式合法

输入：
输入算术表达式

输出：
计算出结果值
"""
def calculate(s):
    s += " "
    nums = []
    op = "+"
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            match op:
                case "+":
                    nums.append(num)
                case "-":
                    nums.append(-num)
                case "*":
                    nums.append(nums.pop() * num)
                case "/":
                    nums.append(int(nums.pop() / num))
            op = ch
            num = 0
    return sum(nums)


if __name__ == '__main__':
    s = "5-3+9*6*(6-10-2)"
    s = s.replace(" ", "")
    while s.count("(") > 0:
        i = s.rfind("(")
        j = s[i:].find(")")
        n = calculate(s[i + 1 : i + j])
        if n < 0:
            a = s[:i].rfind("(")
        s = s[:i] + str() + s[i + j + 1 :]
    ans = calculate(s)
    print(ans)
