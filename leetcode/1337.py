def kWeakestRows(mat, k):
    nums = []
    for i in range(len(mat)):
        nums.append(mat[i].count(1))
    sortNums = nums.copy()
    sortNums.sort()
    ans = [nums.index(sortNums[0])]
    for i in range(1, k):
        if sortNums[i] == sortNums[i - 1]:
            ans.append(ans[-1] + nums[ans[-1] + 1:].index(sortNums[i]) + 1)
        else:
            ans.append(nums.index(sortNums[i]))
    return ans


if __name__ == '__main__':
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k = 3
    ans = kWeakestRows(mat, k)
    print(ans)