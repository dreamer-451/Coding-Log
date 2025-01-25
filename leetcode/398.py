import random


class Solution:

    def __init__(self, nums):
        self.nums = nums
        # self.dictn = dict.fromkeys(nums, [])
        # 不能这么写，通过fromkeys()方法创建字典时，如果直接对所有键赋值，后面修改某一个键值时将同步修改所有键的值
        # 例如：
        # dictn = {1:[], 2:[], 3:[]}
        # dictn[1].append(1)
        # 结果为：
        # dictn = {1:[1], 2:[1], 3:[1]}
        self.dictn = dict.fromkeys(nums)
        for key in self.dictn:
            self.dictn[key] = []

        for i in range(len(nums)):
            self.dictn[nums[i]].append(i)

    def pick(self, target):
        return random.choice(self.dictn[target])


if __name__ == '__main__':
    nums = [1,2,3,3,3]
    target = 3
    obj = Solution(nums)
    param_1 = obj.pick(target)
    param_2 = obj.pick(target)
    param_3 = obj.pick(target)
    print(param_1)
    print(param_2)
    print(param_3)
