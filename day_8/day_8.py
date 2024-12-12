import sys

sys.setrecursionlimit(10 ** 6)
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]
row = len(lines)
col = len(lines[0])

pos = {}
for i in range(row):
    for j in range(col):
        if lines[i][j] != '.':
            if lines[i][j] not in pos:
                pos[lines[i][j]] = []
            pos[lines[i][j]].append((i, j))
antinodes = set()
for key in pos:
    point = pos[key]
    for i, (x, y) in enumerate(point):
        for j in range(i + 1, len(point)):
            x1, y1 = point[j]
            dx, dy = x1 - x, y1 - y
            if dx != 0 or dy != 0:
                # antinodes.add((x1+dx,y1+dy))
                # antinodes.add((x-dx,y-dy))
                nx, ny = x, y
                while 0 <= nx <= row and 0 <= ny <= col:
                    antinodes.add((nx, ny))
                    nx -= dx
                    ny -= dy
                while 0 <= x1 <= row and 0 <= y1 <= col:
                    antinodes.add((x1, y1))
                    x1 += dx
                    y1 += dy
ans = 0
for x, y in antinodes:
    if 0 <= x < row and 0 <= y < col:
        ans += 1
print(ans)
