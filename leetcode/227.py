def calculate(s):
    s = s.replace(" ", "")
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
    s = "3+2*2"
    ans = calculate(s)
    print(ans)