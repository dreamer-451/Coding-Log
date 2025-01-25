def canSeePersonsCount(heights):
    ans = []
    index = []
    stack = []
    for i in range(len(heights)):
        index.append(0)
        while len(stack) > 0 and heights[i] > heights[stack[-1]]:
            index[stack.pop()] = i
        stack.append(i)
    for i in range(len(heights) - 1):
        ans.append(1)
        j = i + 1
        while index[j] != 0 and j < index[i]:
            ans[-1] += 1
            j = index[j]
        if index[i] == 0 and i != len(heights) - 1:
            while index[j] != 0:
                ans[-1] += 1
                j = index[j]
    ans.append(0)
    return ans


if __name__ == '__main__':
    heights = [2, 10, 3, 4, 8]
    ans = canSeePersonsCount(heights)
    print(ans)