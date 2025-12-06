with open("input.txt", 'r') as file:
    total = 0
    for line in file.readlines():
        a = list(map(int, line.strip()))
        b = [a[0]]
        c = [a[-1]]
        for i in a[1:]:
            b.append(max(b[-1], i))
        for i in list(reversed(a))[1:]:
            c.append(max(c[-1], i))
        c.reverse()
        mxm = 0
        for i in range(len(a)-1):
            new = int(str(b[i]) + str(c[i+1]))
            mxm = max(mxm, new)
        total += mxm
        print(a)
        print(b)
        print(c)
        print(mxm, total)