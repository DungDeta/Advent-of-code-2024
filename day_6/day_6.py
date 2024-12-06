import numpy as np
input_file = open('input.txt', 'r')
lines = input_file.readlines()
input_file.close()
matrix = np.array([list(line.strip()) for line in lines])
rows,cols = matrix.shape
stars_x,stars_y=0,0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '^':
            stars_x = i
            stars_y = j
            break
def move(x_in,y_in,direction):
    if direction == '^':
        x_in -= 1
    elif direction == '>':
        y_in += 1
    elif direction == 'v':
        x_in += 1
    elif direction == '<':
        y_in -= 1
    return x_in,y_in
def rotation(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'

def let_move(x, y, matrix):
    visited=set()
    visited.add((x,y,matrix[x,y]))
    while 0 <= x < rows-1 and 0 <= y < cols-1:
        x_new, y_new = move(x, y, matrix[x, y])
        if matrix[x_new, y_new] == '#':
            matrix[x, y] = rotation(matrix[x, y])
        else:
            matrix[x_new, y_new] = matrix[x, y]
            x, y = x_new, y_new
            if (x,y,matrix[x,y]) in visited:
                return 1
            visited.add((x,y,matrix[x,y]))
    return 0
res=0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '.' and (i, j) != (stars_x, stars_y):
            matrix_copy = matrix.copy()
            matrix_copy[i][j] = '#'
            if let_move(stars_x,stars_y,matrix_copy):
                res+=1
    print(res)
print(res)