"""
HJ17 坐标移动

功能:
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

数据范围：
每组输入的字符串长度满足 1 ≤ n ≤ 10000，坐标保证满足 −2^31 ≤ x, y ≤ 2^31 − 1，且数字部分仅含正数

输入：
一行字符串，包含合法坐标和非法坐标
合法坐标为A(或者D或者W或者S) + 数字（两位以内）坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
一个简单的例子 如：A10;S20;W10;D30;X;A1A;B10A11;;A10;

输出：
最终坐标，以逗号分隔
"""

if __name__ == '__main__':
    str = input()
    ops = str.split(";")
    x, y = 0, 0
    for op in ops:
        len_op = len(op)
        if len_op <= 1 or len_op > 3:
            continue
        if op[1:].isdigit():
            match op[0]:
                case "A":
                    x -= int(op[1:])
                case "D":
                    x += int(op[1:])
                case "W":
                    y += int(op[1:])
                case "S":
                    y -= int(op[1:])
    print(f"{x},{y}")
