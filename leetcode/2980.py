# 注意按位或的判断，只要其中一个数为奇数，则其按位或结果的二进制表达末位一定为1
def hasTrailingZeros(nums):
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        if even == 2:
            return True
    return False

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(hasTrailingZeros(nums))
