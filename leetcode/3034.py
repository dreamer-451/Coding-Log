def countMatchingSubarrays(nums, pattern):
    num = 0
    len_n = len(nums)
    len_p = len(pattern)
    ind = 0
    for i in range(len_n - len_p):
        for j in range(len_p):
            match pattern[j]:
                case 1:
                    if nums[i + j + 1] <= nums[i + j]:
                        ind = 1
                        break
                case 0:
                    if nums[i + j + 1] != nums[i + j]:
                        ind = 1
                        break
                case -1:
                    if nums[i + j + 1] >= nums[i + j]:
                        ind = 1
                        break
        if ind == 0:
            num += 1
        ind = 0
    return num


if __name__ == '__main__':
    nums = [1, 4, 4, 1, 3, 5, 5, 3]
    pattern = [1, 0, -1]
    ans = countMatchingSubarrays(nums, pattern)
    print(ans)