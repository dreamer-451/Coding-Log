def addBinary(a, b):
    alist = list(a)
    blist = list(b)
    alist.reverse()
    blist.reverse()
    alen = len(a)
    blen = len(b)
    clist = []
    tmp = 0
    if alen >= blen:
        for i in range(blen):
            clist.append(str((int(alist[i]) + int(blist[i]) + tmp) % 2))
            tmp = (int(alist[i]) + int(blist[i]) + tmp) // 2
        for i in range(blen, alen):
            clist.append(str((int(alist[i]) + tmp) % 2))
            tmp = (int(alist[i]) + tmp) // 2
        if tmp == 1:
            clist.append(str(tmp))
    else:
        for i in range(alen):
            clist.append(str((int(alist[i]) + int(blist[i]) + tmp) % 2))
            tmp = (int(alist[i]) + int(blist[i]) + tmp) // 2
        for i in range(alen, blen):
            clist.append(str((int(blist[i]) + tmp) % 2))
            tmp = (int(blist[i]) + tmp) // 2
        if tmp == 1:
            clist.append(str(tmp))
    clist.reverse()
    c = "".join(clist)
    return c


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    c = addBinary(a, b)
    print(c)