def maxProduct(nums):
    ans = nums[0]
    maxp = minp = 1
    for num in nums:
        maxp, minp = max(num, minp * num, maxp * num), \
            min(num, minp * num, maxp * num)
        ans = max(maxp, ans)
    return ans


if __name__ == '__main__':
    nums = [2,3,-2,4]
    print(maxProduct(nums))
    nums1 = [0, 10, 10]
    print(maxProduct(nums1))