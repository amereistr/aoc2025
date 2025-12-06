invs = [int(str(i) + str(i)) for i in range(900000)]

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
    
    print(total)
