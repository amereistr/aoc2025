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
        start += amt
        start %= 100
        if start == 0:
            total += 1
    
    print(total)