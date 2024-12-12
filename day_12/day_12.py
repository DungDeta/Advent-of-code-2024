import collections
import sys

d4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def to_ractangle(input):
    R = len(input)
    C = max(len(row) for row in input)
    grid = [[''] * C for _ in range(R)]
    for x in range(R):
        for y in range(len(input[x])):
            grid[x][y] = input[x][y]
    return grid


def to_infinite_grid(input, default):
    m = to_ractangle(input)
    row = len(input)
    col = len(input[0])
    grid = collections.defaultdict(lambda: collections.defaultdict(lambda: default))
    for x in range(row):
        for y in range(col):
            grid[x][y] = m[x][y]
    return grid


sys.setrecursionlimit(10 ** 9)
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
lines = file.readlines()
lines=[x.strip() for x in lines]
m = to_infinite_grid(lines, ' ')
file.close()
row = len(lines)
col = len(lines[0])

visited = [[False] * (col+1) for _ in range(row+1)]
res = 0


def DFS(x: int, y: int):
    visited[x][y] = True
    np = set()
    ara = 1
    for dx, dy in d4:
        nx, ny = x + dx, y + dy
        if 0 <= nx < row and 0 <= ny < col and m[x][y] == m[nx][ny] and not visited[nx][ny]:
            pp, aa = DFS(x + dx, y + dy)
            np = np | pp
            ara += aa
        if m[x][y] != m[x + dx][y + dy]:
            np.add((x, y, dx, dy))
    return np, ara


for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            p, a = DFS(i, j)
            pp = 0
            for x, y, dx, dy in p:
                if dx != 0:
                    if (x, y - 1, dx, dy) not in p:
                        pp += 1
                if dy != 0:
                    if (x - 1, y, dx, dy) not in p:
                        pp += 1
            res += a * pp
            print(a*pp)
print(res)
