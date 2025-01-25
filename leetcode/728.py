def selfDividingNumbers(left, right):
    ans = []
    for i in range(left, right + 1):
        num = i
        nums = []
        index = 1
        while num > 0:
            n = num % 10
            if n == 0:
                index = 0
                break
            else:
                nums.append(n)
            num //= 10
        if index == 0:
            continue
        for j in range(len(nums)):
            if i % nums[j] != 0:
                j = -1
                break
        if j != -1:
            ans.append(i)
    return ans


if __name__ == '__main__':
    left = 1
    right = 22
    ans = selfDividingNumbers(left, right)
    print(ans)