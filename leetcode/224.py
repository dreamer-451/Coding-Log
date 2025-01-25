def calculate(s):
    s = s.replace(" ", "")
    s = s.replace("(-", "(0-")
    s += " "
    if s[0] == "-":
        s = "0" + s
    nums = []
    ops = ["+"]
    op = "+"
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '(':
            if ops[-1] == "-":
                if op == "+":
                    op = "-"
                else:
                    op = "+"
            ops.append(op)
            op = "+"
        else:
            if ops[-1] == "-":
                num = -num
            if op == "+":
                nums.append(num)
            else:
                nums.append(-num)
            if ch == ")":
                op = ops.pop()
            else:
                op = ch
            num = 0
    return sum(nums)


if __name__ == '__main__':
    s = "- (3 + (4 + 5))"
    ans = calculate(s)
    print(ans)