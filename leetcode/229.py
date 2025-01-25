def majorityElement(nums):
    ans = []
    nums.sort()
    length = len(nums)
    i = 0
    if length < 3:
        while i < length:
            l = nums.count(nums[i])
            ans.append(nums[i])
            i += l
    else:
        while i < length - length // 3:
            l = nums.count(nums[i])
            if l > length // 3:
                ans.append(nums[i])
            i += l
    return ans


if __name__ == '__main__':
    nums = [3,2,2,2,3]
    ans = majorityElement(nums)
    print(ans)