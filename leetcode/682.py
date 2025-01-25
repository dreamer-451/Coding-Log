def calPoints(operations):
    sum = 0
    pts = []
    for i in range(len(operations)):
        match operations[i]:
            case "+":
                pts.append(pts[-1] + pts[-2])
            case "D":
                pts.append(2 * pts[-1])
            case "C":
                pts.pop()
            case _:
                pts.append(int(operations[i]))
    for pt in pts:
        sum += pt
    return sum


if __name__ == '__main__':
    operations = ["5", "2", "C", "D", "+"]
    sum = calPoints(operations)
    print(sum)