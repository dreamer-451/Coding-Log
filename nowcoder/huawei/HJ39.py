"""
HJ39 判断两个IP是否属于同一子网

功能:
IP地址是由4个0-255之间的整数构成的，用"."符号相连。
二进制的IP地址格式有32位，例如：10000011，01101011，00000011，00011000;每八位用十进制表示就是131.107.3.24
子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
子网掩码与IP地址结构相同，是32位二进制数，由1和0组成，且1和0分别连续，其中网络号部分全为“1”和主机号部分全为“0”。
你可以简单的认为子网掩码是一串连续的1和一串连续的0拼接而成的32位二进制数，左边部分都是1，右边部分都是0。
利用子网掩码可以判断两台主机是否中同一子网中。
若两台主机的IP地址分别与它们的子网掩码进行逻辑“与”运算（按位与/AND）后的结果相同，则说明这两台主机在同一子网中。

输入一个子网掩码以及两个ip地址，判断这两个ip地址是否是一个子网络。
若IP地址或子网掩码格式非法则输出1，若IP1与IP2属于同一子网络输出0，若IP1与IP2不属于同一子网络输出2。

注:
有效掩码与IP的性质为：
1. 掩码与IP每一段在 0 - 255 之间
2. 掩码的二进制字符串前缀为网络号，都由‘1’组成；后缀为主机号，都由'0'组成

输入：
3行输入，第1行是输入子网掩码、第2，3行是输入两个ip地址

输出：
若IP地址或子网掩码格式非法则输出1，
若IP1与IP2属于同一子网络输出0，
若IP1与IP2不属于同一子网络输出2
"""
def check(mask, ip1, ip2):
    # 若子网掩码或IP地址不是4字段，则为非法格式
    if len(mask) != 4 or len(ip1) != 4 or len(ip2) != 4:
        return 1
    ip1_mask = []
    ip2_mask = []
    for i in range(4):
        # 判断子网掩码mask
        # 字段为空，则非法
        if len(mask[i]) == 0:
            return 1
        # 字段小于0，或大于255，则非法
        elif int(mask[i]) > 255 or int(mask[i]) < 0:
            return 1
        # 判断子网掩码是否为连续1接连续0组成
        elif 0 < int(mask[i]) <= 255:
            mask[i] = int(mask[i])
            temp = bin(mask[i])[2:].zfill(8)
            if i != 0 and mask[i - 1] != 255:
                return 1
            if mask[i] != 255 and "01" in temp:
                return 1
        else:
            mask[i] = int(mask[i])
        # 判断IP地址，字段为空或含非数字字符，字段值大于255或小于0，均为非法
        if len(ip1[i]) == 0 or not ip1[i].isdigit() or int(ip1[i]) > 255 or int(ip1[i]) < 0:
            return 1
        else:
            ip1[i] = int(ip1[i])
        # 判断IP地址，字段为空或含非数字字符，字段值大于255或小于0，均为非法
        if len(ip2[i]) == 0 or not ip2[i].isdigit() or int(ip2[i]) > 255 or int(ip2[i]) < 0:
            return 1
        else:
            ip2[i] = int(ip2[i])
        # 子网掩码与IP地址对应字段求按位与(and,&）
        ip1_mask.append(mask[i] & ip1[i])
        ip2_mask.append(mask[i] & ip2[i])
    # 判断IP地址是否属于同一子网
    for i in range(4):
        if ip1_mask[i] != ip2_mask[i]:
            return 2
    return 0


if __name__ == '__main__':
    while True:
        try:
            mask = input().split(".")
            ip1 = input().split(".")
            ip2 = input().split(".")
            ans = check(mask, ip1, ip2)
            print(ans)
        except:
            break
