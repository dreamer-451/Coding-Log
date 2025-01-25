import string
def makeGood(s):
    i = 0
    while i < len(s) - 1:
        if s[i] in string.ascii_lowercase and s[i + 1] == s[i].upper():
            s = s[:i] + s[i + 2:]
            if i > 0:
                i -= 1
        elif s[i] in string.ascii_uppercase and s[i + 1] == s[i].lower():
            s = s[:i] + s[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    return s


if __name__ == '__main__':
    s = "leEeetcode"
    print(makeGood(s))
    t = "abBAcC"
    print(makeGood(t))