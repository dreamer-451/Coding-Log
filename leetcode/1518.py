def numWaterBottles(numBottles, numExchange):
    empty = 0
    full = numBottles
    while full > 0:
        bottle = full + empty
        empty = bottle % numExchange
        full = (bottle - empty) // numExchange
        numBottles += full
    return numBottles


if __name__ == '__main__':
    numBottles = 15
    numExchange = 4
    bottle = numWaterBottles(numBottles, numExchange)
    print(bottle)