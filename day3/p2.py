with open("input.txt", 'r') as file:
    total = 0
    for line in file.readlines():
        a = list(map(int, line.strip()))
        left = 12
        idx = 0
        final = []
        while left > 0:
            # print(idx, left, a[idx:(len(a)-left+1)])
            mxm = max(a[idx:(len(a)-left+1)])
            jump = a[idx:(len(a)-left+1)].index(mxm)
            final.append(mxm)
            idx += jump + 1
            left -= 1
        res = int(''.join(map(str, final)))
        total += res
        print(res, total)