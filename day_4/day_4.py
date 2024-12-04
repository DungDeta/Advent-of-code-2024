import numpy as np
with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
matrix = np.array([list(line) for line in lines])
rows, cols = matrix.shape
def generate_all_lines(matrix):
    lines = []

    # 1. Hàng ngang
    for row in matrix:
        lines.append(''.join(row))

    # 2. Cột dọc
    for col in matrix.T:  # Transpose ma trận để duyệt theo cột
        lines.append(''.join(col))

    # 3. Đường chéo trái trên → phải dưới
    for offset in range(-rows + 1, cols):  # Offset từ -(rows-1) đến cols-1
        diag = matrix.diagonal(offset)
        lines.append(''.join(diag))

    # 4. Đường chéo phải trên → trái dưới
    flipped_matrix = np.fliplr(matrix)  # Lật ma trận theo chiều ngang
    for offset in range(-rows + 1, cols):  # Offset như trên
        diag = flipped_matrix.diagonal(offset)
        lines.append(''.join(diag))

    return lines
find_words = ['XMAS', 'SAMX']
total_count = 0
full_lines=generate_all_lines(matrix)
for word in find_words:
    for line in full_lines:
        total_count += line.count(word)
print(total_count)
word='MAS'
count=0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]=='A':
            good=0
            curr=[]
            for d in range(-1,2):
                nx,ny=i+d,j+d
                if 0<=nx<rows and 0<=ny<cols:
                    curr.append(lines[nx][ny])
                if ''.join(curr)==word or ''.join(curr)==word[::-1]:
                    good+=1
            curr=[]
            for d in range(-1,2):
                nx,ny=i+d,j-d
                if 0<=nx<rows and 0<=ny<cols:
                    curr.append(lines[nx][ny])
                if ''.join(curr)==word or ''.join(curr)==word[::-1]:
                    good+=1
            if good==2:
                count+=1
print(count)