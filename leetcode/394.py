import string
def decodeString(s):
    ans = ""
    list_s = []  # 需重复的小写字母子序列
    index_s = []  # 需重复的子序列最后一个小写字母对应下标
    list_d = []  # 子序列对应的重复次数
    stack = []  # 重复子序列间隔符号 [ 对应下标
    i = 0
    while i < len(s):
        if s[i] == '[':  # 后跟需重复的子序列
            stack.append(i)
            i += 1
        elif s[i] == ']':
            stack.pop()
            if len(stack) == 0: # 除当前子序列外不存在需重复的序列
                ans += list_s.pop() * list_d.pop()
                index_s.pop()
            else: # 有其他需重复的子序列
                temp = list_s.pop() * list_d.pop()
                if len(list_s) == 0 or stack[-1] > index_s[-2]: # 该子序列在执行重复操作后生成的序列仍需重复且需执行的重复操作与其余以存储的需重复子序列不同
                    list_s.append(temp)
                else: # 重复操作生成的子序列需执行的重复操作与已存储的某一子序列相同，故将之合并
                    list_s[-1] += temp
                    index_s.pop(-2)
            i += 1
        elif s[i] in string.digits: # 存储对应重复子序列的重复次数
            for j in range(i, len(s)):
                if s[j] not in string.digits:
                    break
            list_d.append(int(s[i:j]))
            i = j
        else: # 小写字母子序列
            for j in range(i, len(s)):
                if s[j] not in string.ascii_lowercase:
                    break
            if len(stack) == 0: # 该序列无需重复，可直接添加入答案序列中
                if i == j == len(s) - 1:
                    ans += s[i:]
                    i = j + 1
                else:
                    ans += s[i:j]
                    i = j
            else: # 该序列需执行重复操作
                if len(list_s) == 0 or stack[-1] > index_s[-1]: # 该序列需执行的重复操作与以存储的子序列不同
                    list_s.append(s[i:j])
                    index_s.append(j - 1)
                else: # 该序列需执行的重复操作与已存储的某一子序列相同，故将之合并
                    list_s[-1] += s[i:j]
                    index_s[-1] = j - 1
                i = j
    return ans


if __name__ == '__main__':
    s = "2[abc]3[cd]ef"
    ans = decodeString(s)
    print(ans)
    s1 = "3[a2[c]]"
    ans1 = decodeString(s1)
    print(ans1)
    s2 = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    ans2 = decodeString(s2)
    print(ans2)
    s3 = "sd2[f2[e]g]i"
    ans3 = decodeString(s3)
    print(ans3)