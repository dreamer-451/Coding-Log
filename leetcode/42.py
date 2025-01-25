def trap(height):
    water = 0
    l = len(height)
    left, right = [height[0]] + [0] * (l - 1), [0] * (l - 1) + [height[-1]]
    for i in range(1, l):
        # 查找该点处左侧最高值
        left[i] = max(height[i], left[i - 1])
        # 查找该点处右侧最高值
        right[l - 1 - i] = max(height[l - 1 - i], right[l - i])
    for i in range(l):
        water += min(left[i], right[i]) - height[i]
    return water


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ans = trap(height)
    print(ans)