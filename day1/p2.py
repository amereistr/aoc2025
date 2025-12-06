with open("input.txt", 'r') as file:
    rots = []
    for line in file.readlines():
        if line.strip() == "":
            continue
        direction = (-1) ** (line[0] == 'L')
        rots.append(direction * int(line[1:]))
    
    start = 50
    total = 0
    for amt in rots:
        while (amt > 0):
            amt -= 1
            start = (start + 1) % 100
            if start == 0: total += 1
        while (amt < 0):
            amt += 1
            start = (start - 1) % 100
            if start == 0: total += 1
        print(start, total)
    
    print(total)        