def canCompleteCircuit(gas, cost):
    for i in range(len(gas)):
        gas[i] -= cost[i]
    init = -1
    i = 0
    while i < len(gas):
        if gas[i] < 0:
            i += 1
            continue
        cirgas = gas[i:] + gas[:i]
        index = 0
        for j in range(1, len(cirgas)):
            cirgas[j] += cirgas[j - 1]
            if cirgas[j] < 0:
                index = 1
                i += j
                break
        if index == 0:
            init = i
            break
    return init


if __name__ == '__main__':
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    ans = canCompleteCircuit(gas, cost)
    print(ans)