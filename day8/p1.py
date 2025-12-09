from math import sqrt

def dist(a, b):
    acc = 0
    for x, y in zip(a, b):
        acc += (x - y) ** 2
    return sqrt(acc)


with open("input.txt", 'r') as file:
    to_include = 1000

    positions = []
    
    for line in file.readlines():
        a, b, c = map(int, line.strip().split(","))
        positions.append((a, b, c))
    
    edges = [
        (positions[idx1], positions[idx2], dist(positions[idx1], positions[idx2]))
        for idx1 in range(len(positions))
        for idx2 in range(idx1+1, len(positions))]
    edges.sort(key=lambda x: x[2])
    
    included = edges[:to_include]

    print(positions)
    for e in included:
        print(e)
    
    adjacency_list = {}
    for e in included:
        if e[0] not in adjacency_list:
            adjacency_list[e[0]] = {e[0]}
        if e[1] not in adjacency_list:
            adjacency_list[e[1]] = {e[1]}
        for twin in list(adjacency_list[e[0]]):
            adjacency_list[twin].update(adjacency_list[e[1]])
        for twin in list(adjacency_list[e[1]]):
            adjacency_list[twin].update(adjacency_list[e[0]])
    
    for k, v in adjacency_list.items():
        print(k, v)

    visited = {a:False for a in positions}
    stack = [a for a in positions]
    circs_lens = []
    while len(stack) > 0:
        tos = stack.pop()
        if (visited[tos]): continue
        visited[tos] = True
        
        if tos not in adjacency_list:
            circs_lens.append(1)
            continue

        adjs = adjacency_list[tos]
        circs_lens.append(len(adjs))
        for e in adjs:
            visited[e] = True

    
    circs_lens.sort(reverse=True)
    print(circs_lens)
    if len(circs_lens) >= 3:
        print(circs_lens[0] * circs_lens[1] * circs_lens[2])
