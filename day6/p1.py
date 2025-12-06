with open("input.txt", 'r') as file:
    nums = []
    for _ in range(4):
        line = list(map(int,file.readline().strip().split()))
        nums.append(line)

    ops = file.readline().strip().split()
    
    total = 0
    for op, one, two, three, four in zip(ops, *nums):
        if (op == "+"):
            total += one + two + three + four
        if (op == "*"):
            total += one * two * three * four
    print(total)