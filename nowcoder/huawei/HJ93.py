"""
HJ93 数组分组

功能:
输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，
并且，所有5的倍数必须在其中一个组中，
    所有3的倍数在另一个组中（不包括5的倍数），
    不是5的倍数也不是3的倍数能放在任意一组，
可以将数组分为空数组，能满足以上条件，输出true；不满足时输出false。

数据范围：
每个数组大小满足 1 ≤ n ≤ 50，输入的数据大小满足 ∣val∣ ≤ 500

输入：
第一行是数据个数，第二行是输入的数据

输出：
返回true或者false
"""

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    nums0 = []
    nums3 = []
    nums5 = []
    for num in nums:
        if num % 5 == 0:
            nums5.append(num)
        elif num % 3 == 0:
            nums3.append(num)
        else:
            nums0.append(num)
    sum3 = sum(nums3)
    sum5 = sum(nums5)
    # 求出3倍数组和5倍数组初始和的差值
    ans = [sum3 - sum5]
    # 对差值进行处理，分别取其余数组中的每个数的正值和负值与差值结果进行迭代，
    # 正负值分别代表分到3倍数组或5倍数组
    for n in nums0:
        temp0 = []
        temp1 = []
        for a in ans:
            temp0.append(a - n)
            temp1.append(a + n)
        ans = temp0 + temp1
    # 判断 0 是否存在于处理完其余数组中所有数生成的结果集中
    if 0 in ans:
        print("true")
    else:
        print("false")
