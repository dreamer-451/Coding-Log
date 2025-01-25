def pivotIndex(nums):
    lsum = [0]
    rsum = [0]
    for i in range(1, len(nums)):
        lsum.append(lsum[-1] + nums[i-1])
        rsum.append(rsum[-1] + nums[ - i])
    rsum.reverse()
    for i in range(len(nums)):
        if lsum[i] == rsum[i]:
            return i
    return -1


if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    index = pivotIndex(nums)
    print(index)