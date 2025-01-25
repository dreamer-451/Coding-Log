def kLengthApart(nums, k):
    if 1 not in nums:
        return True
    s = nums.index(1)
    temp = k
    for i in range(s + 1, len(nums)):
        if nums[i] == 1:
            if temp <= 0:
                temp = k
            else:
                return False
        else:
            temp -= 1
    return True


if __name__ == '__main__':
    nums = [1,0,0,0,1,0,0,1]
    k = 2
    print(kLengthApart(nums, k))