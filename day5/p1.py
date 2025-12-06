with open("input.txt", 'r') as file:
    ids_range = []
    while True:
        line = file.readline()
        if line.strip() == "": break
        a, b = line.strip().split("-")
        ids_range.append((int(a), int(b)))
    
    total = 0
    for line in file.readlines():
        a = int(line.strip())
        for l, r in ids_range:
            if l <= a and a <= r:
                total += 1
                break
    
    print(total)