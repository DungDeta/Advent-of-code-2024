import collections as c
import sys

import numpy as np

sys.setrecursionlimit(10 ** 6)
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
lines = file.readlines()
lines = [line.rstrip() for line in lines]
num = [[int(i) for i in line] for line in lines]
matrix = np.array(num)
row, col = matrix.shape
file.close()


def BFS(x: int, y: int) -> int:
    visited = set()
    queue = c.deque()
    queue.append((x, y))
    visited.add((x, y))
    count = c.Counter()
    count[(x, y)] = 1
    res = 0
    while queue:
        x, y = queue.popleft()
        if matrix[x][y] == 9:
            res += count[(x, y)]
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < row and 0 <= j < col and matrix[i][j] == matrix[x][y] + 1 and (i, j) not in visited:
                queue.append((i, j))
                visited.add((i, j))
            if 0 <= i < row and 0 <= j < col and matrix[i][j] == matrix[x][y] + 1:
                count[(i, j)] += count[(x, y)]
    return res


res_1 = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            res_1 += BFS(i, j)
print(res_1)
