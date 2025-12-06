invs =\
    [int(str(i) * 2 ) for i in range(200000)] + \
    [int(str(i) * 3 ) for i in range(200000)] + \
    [int(str(i) * 4 ) for i in range(20000)] + \
    [int(str(i) * 5 ) for i in range(2000)] + \
    [int(str(i) * 6 ) for i in range(200)] + \
    [int(str(i) * 7 ) for i in range(200)] + \
    [int(str(i) * 8 ) for i in range(20)] + \
    [int(str(i) * 9 ) for i in range(20)] + \
    [int(str(i) * 10 ) for i in range(20)]

invs = sorted(list(set(invs)))

def bin_search(v, lower_bound=False):
    low = 0
    high = len(invs) - 1

    if lower_bound and invs[0] > v: return 0
    if not lower_bound and invs[high] < v: return high

    while high - low > 1:
        mid = (low + high) // 2
        if v > invs[mid]:
            low = mid
        else:
            high = mid
        
        # print(low, mid, high)
    
    if invs[low] == v: return low
    if invs[high] == v: return high
    
    if lower_bound:
        return high
    else:
        return low


# a = bin_search(11)
# print(a)
# print(invs[a])
# a = bin_search(22, False)
# print(a)
# print(invs[a])

with open("input.txt", 'r') as file:
    ids_range = []
    for x in file.readline().split(","):
        a, b = x.split("-")
        ids_range.append((int(a), int(b)))
    

    total = 0
    for l,h in ids_range:
        low_idx = bin_search(l, True)
        high_idx = bin_search(h, False)
        total += sum(invs[low_idx:high_idx+1])

        print(l, low_idx, h, high_idx, total)
        print(invs[low_idx:high_idx+1])
    
    print(total)
