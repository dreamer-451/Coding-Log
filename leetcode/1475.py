def finalPrices(prices):
    temp = []
    ans = []
    for i in range(len(prices)):
        ans.append(prices[i])
        while len(temp) > 0 and prices[i] <= prices[temp[-1]]:
            ans[temp.pop()] -= prices[i]
        temp.append(i)
    return ans


if __name__ == '__main__':
    prices = [8, 4, 6, 2, 3]
    ans = finalPrices(prices)
    print(ans)