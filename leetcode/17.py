def letterCombinations(digits):
    if len(digits) == 0:
        return []
    dig_al = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9':'wxyz',
    }
    ans = ['']
    for digit in digits:
        lans = len(ans)
        ll = len(dig_al[digit])
        ans *= ll
        for letter in dig_al[digit]:
            for i in range(lans * dig_al[digit].index(letter), lans * (dig_al[digit].index(letter) + 1)):
                ans[i] += letter
    return ans


if __name__ == '__main__':
    digits = '9999'
    ans = letterCombinations(digits)
    print(ans)