import numpy as np
from scipy.signal import convolve2d

kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])


with open("input.txt", 'r') as file:
    grid = []
    
    for line in file.readlines():
        a = [1 if a == '@' else 0 for a in line.strip()]
        grid.append(a)
    
    prev_total = -1
    total = 0

    while prev_total != total:
        grid = np.array(grid)
        out = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
        is_less = out < 4
        res = grid & is_less

        prev_total = total
        total += sum(sum(res))

        grid -= res
        # print(grid)
        # print(res)
        print(total)