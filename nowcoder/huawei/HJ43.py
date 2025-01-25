"""
HJ43 迷宫问题

功能:
定义一个二维数组 N*M ，如 5 × 5 数组下所示：
int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};
它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，
要求编程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。

数据范围：
2 ≤ n,m ≤ 10  ， 输入的内容只包含 0 ≤ val ≤ 1

输入：
输入两个整数，分别表示二维数组的行数，列数。
再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出：
左上角到右下角的最短路径
每行输出路径中的一个坐标点，格式为：(x,y)
"""

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    maze = []
    for i in range(n):
        maze.append(list(map(int, input().split())))
    i, j = 0, 0
    points = []
    directions = [1, 2, 3, 4]
    dirs = []
    while i != n - 1 or j != m - 1:
        if (i, j) not in points:
            points.append((i, j))
        for d in directions:
            if d == 1 and i != n - 1 and maze[i + 1][j] != 1:
                if (i + 1, j) in points:
                    maze[i][j] = 1
                    points.pop()
                    dirs.pop()
                else:
                    dirs.append(d)
                i += 1
                directions.remove(5 - dirs[-1])
                directions.append(5 - dirs[-1])
                break
            if d == 2 and j != m - 1 and maze[i][j + 1] != 1:
                if (i, j + 1) in points:
                    maze[i][j] = 1
                    points.pop()
                    dirs.pop()
                else:
                    dirs.append(d)
                j += 1
                directions.remove(5 - dirs[-1])
                directions.append(5 - dirs[-1])
                break
            if d == 3 and j != 0 and maze[i][j - 1] != 1:
                if (i, j - 1) in points:
                    maze[i][j] = 1
                    points.pop()
                    dirs.pop()
                else:
                    dirs.append(d)
                j -= 1
                directions.remove(5 - dirs[-1])
                directions.append(5 - dirs[-1])
                break
            if d == 4 and i != 0 and maze[i - 1][j] != 1:
                if (i - 1, j) in points:
                    maze[i][j] = 1
                    points.pop()
                    dirs.pop()
                else:
                    dirs.append(d)
                i -= 1
                directions.remove(5 - dirs[-1])
                directions.append(5 - dirs[-1])
                break
    points.append((i, j))
    for point in points:
        print(f"({point[0]},{point[1]})")
