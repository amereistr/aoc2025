from math import sqrt

def dist(a, b):
    acc = 0
    for x, y in zip(a, b):
        acc += (x - y) ** 2
    return sqrt(acc)


with open("input.txt", 'r') as file:
    # to_include = 1000

    positions = []
    
    for line in file.readlines():
        a, b, c = map(int, line.strip().split(","))
        positions.append((a, b, c))
    
    edges = [
        (positions[idx1], positions[idx2], dist(positions[idx1], positions[idx2]))
        for idx1 in range(len(positions))
        for idx2 in range(idx1+1, len(positions))]
    edges.sort(key=lambda x: x[2])

    # print(positions)
    # for e in included:
    #     print(e)

    print("doing it now")
    
    adjacency_list = {}
    for e in edges:
        if e[0] not in adjacency_list:
            adjacency_list[e[0]] = {e[0]}
        if e[1] not in adjacency_list:
            adjacency_list[e[1]] = {e[1]}
        for twin in list(adjacency_list[e[0]]):
            adjacency_list[twin].update(adjacency_list[e[1]])
        for twin in list(adjacency_list[e[1]]):
            adjacency_list[twin].update(adjacency_list[e[0]])
        
        if len(adjacency_list[e[0]]) == len(positions):
            print(e)
            print(e[0][0] * e[1][0])
            break
