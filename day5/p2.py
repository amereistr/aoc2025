with open("input.txt", 'r') as file:
    ids_range = []
    while True:
        inx += 1
        line = file.readline()
        if line.strip() == "": break
        a, b = map(int, line.strip().split("-"))
        
        ids_range.sort(key=lambda x: (x[0], x[1]))
        for l, r in ids_range:
            if l <= a and a <= r:
                a = r + 1
        ids_range.sort(key=lambda x: (x[0], x[1]), reverse=True)
        for l, r in ids_range:
            if l <= b and b <= r:
                b = l - 1
        if a > b: continue

        remove = []
        for l, r in ids_range:
            if a <= l and r <= b:
                remove.append((l,r))
        for i in remove:
            ids_range.remove(i)

        ids_range.append((int(a), int(b)))

    total = 0
    for l, r in ids_range:
        total += r - l + 1

    print(total)