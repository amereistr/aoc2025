from functools import reduce
from operator import add, mul

with open("input.txt", 'r') as file:
    nums = []
    for _ in range(4):
        nums.append(file.readline())
    ops = file.readline()
    
    total = 0
    op = ""
    currs = []
    for op_chr, *num in zip(ops, *nums):    # python black magic
        print(op_chr, num)
        if op == "":
            op = op_chr

        n = "".join(num)
        n.replace(" ", "")
        if n.strip() == "":
            if (op == "+"):
                res = reduce(add, currs, 0)
            if (op == "*"):
                res = reduce(mul, currs, 1)
            total += res
            op = ""
            currs = []
            
            print(res, total)
        else:
            currs.append(int(n))
    
    if (op == "+"):
        res = reduce(add, currs, 0)
    if (op == "*"):
        res = reduce(mul, currs, 1)
    total += res
            
    print(res, total)