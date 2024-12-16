import numpy as np

d4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Đọc dữ liệu
test = False
if test:
    file = open('testcase.txt', 'r')
else:
    file = open('input.txt', 'r')
# lines = file.readlines()
# file.close()
# lines = [x.strip() for x in lines]
#
# matrix = []
# i = 0
# while lines[i] != '':
#     matrix.append(list(lines[i]))
#     i += 1
# matrix = np.array(matrix)
# moves = "".join(lines[i+1:])
# row, col = len(matrix), len(matrix[0])
# m_2=[]
# for row in matrix:
#     nrow= []
#     for cell in row:
#         if cell=='#':
#             nrow.append('#')
#             nrow.append('#')
#         elif cell=='O':
#             nrow.append('[')
#             nrow.append(']')
#         elif cell=='@':
#             nrow.append('@')
#             nrow.append('.')
#         else:
#             nrow.append('.')
#             nrow.append('.')
#     m_2.append(nrow)
# matrix= m_2
# row, col = len(matrix), len(matrix[0])
# pos = [0, 0]
# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == '@':
#             pos = [i, j]
#             break
# step = '><v^'
#
# for m in moves:
#     dx, dy = d4[step.index(m)]
#     c2m=[(pos[0], pos[1])]
#     i=0
#     impos=False
#     while i < len(c2m):
#         x,y=c2m[i]
#         nx,ny=x+dx, y+dy
#         if matrix[nx][ny] in ['O[]']:
#             if (nx, ny) not in c2m:
#                 c2m.append((nx, ny))
#             if matrix[nx][ny]=='[':
#                 if (nx,ny+1) not in c2m:
#                     c2m.append((nx,ny+1))
#             if matrix[nx][ny]==']':
#                 if (nx,ny-1) not in c2m:
#                     c2m.append((nx,ny-1))
#         elif matrix[nx][ny]=='#':
#             impos=True
#             break
#         i+=1
#     if impos:
#         continue
#     new_grid=[[matrix[i][j] for j in range(col)] for i in range(row)]
#     for x,y in c2m:
#         new_grid[x][y]='.'
#     for x,y in c2m:
#         new_grid[x+dx][y+dy]=matrix[x][y]
#     matrix=new_grid
#     pos=[pos[0]+dx, pos[1]+dy]
#     # if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == '.':
#     #     pos = [nx, ny]
#     #     continue
#     # if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == '#':
#     #     continue
#     # if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 'O':
#     #     fx, fy = nx, ny
#     #     while 0 <= fx < row and 0 <= fy < col and matrix[fx][fy] == 'O':
#     #         fx += dx
#     #         fy += dy
#     #     if not (0 <= fx < row and 0 <= fy < col) or matrix[fx][fy] == '#':
#     #         continue
#     #     if matrix[fx][fy] == '.':
#     #         matrix[fx][fy] = 'O'
#     #         matrix[nx][ny] = '.'
#     #         pos = [nx, ny]
#
# for i in range(row):
#     print(''.join(matrix[i]))
#
# res = 0
# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] != '[':
#             continue
#         res += 100*i + j
#
# print(res)
map,moves= file.read().split('\n\n')
map_lines = map.split('\n')
rows = len(map_lines)
cols = len(map_lines[0]) * 2
walls = set()
left_boxes = set()
right_boxes = set()
for i, L in enumerate(map_lines):
    for j, c in enumerate(L):
        if c == '#':
            walls.add((i, 2 * j))
            walls.add((i, 2 * j + 1))
        elif c == 'O':
            left_boxes.add((i, 2 * j))
            right_boxes.add((i, 2 * j + 1))
        elif c == '@':
            robot = (i, 2 * j)


# read in the moves made by the robot
move_lines = moves.split('\n')
for L in move_lines:
    for c in L:
        if c == '^':
            # build a list of robot and boxes that will be
            # pushed up by robot in its current position
            chain = {robot}
            boxes_to_process = set()
            i = robot[0]
            j = robot[1]
            i -= 1
            if (i,j) in walls:
                continue
            elif (i,j) in left_boxes:
                boxes_to_process.add((i,j))
                boxes_to_process.add((i,j+1))
            elif (i,j) in right_boxes:
                boxes_to_process.add((i,j-1))
                boxes_to_process.add((i,j))

            wall_flag = False
            while(boxes_to_process):
                b = boxes_to_process.pop()
                chain.add(b)
                i = b[0]
                j = b[1]
                i -= 1
                if (i,j) in walls:
                    wall_flag = True
                    continue
                elif (i,j) in left_boxes:
                    boxes_to_process.add((i,j))
                    boxes_to_process.add((i,j+1))
                elif (i,j) in right_boxes:
                    boxes_to_process.add((i,j))
                    boxes_to_process.add((i,j-1))
            if wall_flag:
                continue

            # move chain of objects upward one space
            old_left_boxes = set()
            new_left_boxes = set()
            old_right_boxes = set()
            new_right_boxes = set()
            for b in chain:
                if b == robot:
                    new_robot = (robot[0] - 1, robot[1])
                elif b in left_boxes:
                    old_left_boxes.add(b)
                    new_left_boxes.add((b[0] - 1, b[1]))
                else:
                    old_right_boxes.add(b)
                    new_right_boxes.add((b[0] - 1, b[1]))
            robot = new_robot
            left_boxes -= old_left_boxes
            left_boxes |= new_left_boxes
            right_boxes -= old_right_boxes
            right_boxes |= new_right_boxes

        elif c == '>':
            # build a list of robot and boxes that will be
            # pushed to the right by robot in its current position
            chain = [robot]
            i = robot[0]
            j = robot[1]
            j += 1
            while (i,j) in left_boxes:
                chain.insert(0, (i,j))
                chain.insert(0, (i,j+1))
                j += 2
            # move chain of objects rightward one space if possible
            if not (i,j) in walls:
                for b in chain[:-1:2]:
                    right_boxes.remove(b)
                    right_boxes.add((b[0], b[1] + 1))
                    left_boxes.remove((b[0], b[1] - 1))
                    left_boxes.add((b[0], b[1]))
                robot = (robot[0], robot[1] + 1)

        elif c == 'v':
            # build a list of robot and boxes that will be
            # pushed down by robot in its current position
            chain = {robot}
            boxes_to_process = set()
            i = robot[0]
            j = robot[1]
            i += 1
            if (i,j) in walls:
                continue
            elif (i,j) in left_boxes:
                boxes_to_process.add((i,j))
                boxes_to_process.add((i,j+1))
            elif (i,j) in right_boxes:
                boxes_to_process.add((i,j-1))
                boxes_to_process.add((i,j))

            wall_flag = False
            while(boxes_to_process):
                b = boxes_to_process.pop()
                chain.add(b)
                i = b[0]
                j = b[1]
                i += 1
                if (i,j) in walls:
                    wall_flag = True
                    continue
                elif (i,j) in left_boxes:
                    boxes_to_process.add((i,j))
                    boxes_to_process.add((i,j+1))
                elif (i,j) in right_boxes:
                    boxes_to_process.add((i,j))
                    boxes_to_process.add((i,j-1))
            if wall_flag:
                continue

            # move chain of objects downward one space
            old_left_boxes = set()
            new_left_boxes = set()
            old_right_boxes = set()
            new_right_boxes = set()
            for b in chain:
                if b == robot:
                    new_robot = (robot[0] + 1, robot[1])
                elif b in left_boxes:
                    old_left_boxes.add(b)
                    new_left_boxes.add((b[0] + 1, b[1]))
                else:
                    old_right_boxes.add(b)
                    new_right_boxes.add((b[0] + 1, b[1]))
            robot = new_robot
            left_boxes -= old_left_boxes
            left_boxes |= new_left_boxes
            right_boxes -= old_right_boxes
            right_boxes |= new_right_boxes

        else:       # c == '<'
            # build a list of robot and boxes that will be
            # pushed to the left by robot in its current position
            chain = [robot]
            i = robot[0]
            j = robot[1]
            j -= 1

            while (i,j) in right_boxes:
                chain.insert(0, (i,j))
                chain.insert(0, (i,j-1))
                j -= 2
            # move chain of objects rightward one space if possible
            if not (i,j) in walls:
                for b in chain[:-1:2]:
                    left_boxes.remove(b)
                    left_boxes.add((b[0], b[1] - 1))
                    right_boxes.remove((b[0], b[1] + 1))
                    right_boxes.add(b)
                robot = (robot[0], robot[1] - 1)

# calculate GPS sum
total = 0
for b in left_boxes:
    total += 100 * b[0] + b[1]
print(total)