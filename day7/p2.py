with open("input.txt", 'r') as file:
    grid = []
    
    for line in file.readlines():
        a = [1 if (a == 'S' or a == "^") else 0 for a in line.strip()]
        grid.append(a)
    
    split = 0
    starting = grid[0]
    for line in grid[1:]:
        nxt = [0 for _ in starting]
        for idx in range(len(starting)):
            if line[idx] == 1 and starting[idx] >= 1:
                split += 1
                nxt[idx-1] += starting[idx]
                nxt[idx+1] += starting[idx]
            elif line[idx] == 0 and starting[idx] >= 1:
                nxt[idx] += starting[idx]
        starting = nxt
        print(nxt)
    
    print(starting)
    print(sum(starting))
    print(split)