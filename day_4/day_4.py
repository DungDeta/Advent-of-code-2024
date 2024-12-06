import numpy as np
import sys
sys.setrecursionlimit(10**6)

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
matrix = np.array([list(line) for line in lines])
rows, cols = matrix.shape


def generate_all_lines(matrix):  # Dùng numpy sinh ra toàn bộ các dòng cần kiểm tra
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
full_lines = generate_all_lines(matrix)
for word in find_words:
    for line in full_lines:
        total_count += line.count(word)
print(total_count)
word = 'MAS'
count = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 'A':
            good = 0
            curr = []
            for d in range(-1, 2):  # d=-1,0,1
                nx, ny = i + d, j + d  # d=-1: (i-1,j-1) d=0: (i,j) d=1: (i+1,j+1) Duyệt 3 ô liền kề trên theo đường chéo
                if 0 <= nx < rows and 0 <= ny < cols:
                    curr.append(lines[nx][ny])
                if ''.join(curr) == word or ''.join(curr) == word[::-1]:  # Kiểm tra xem có từ cần tìm không
                    good += 1
            curr = []
            for d in range(-1, 2):
                nx, ny = i + d, j - d  # d=-1: (i-1,j+1) d=0: (i,j) d=1: (i+1,j-1) Duyệt 3 ô liền kề dưới theo đường chéo
                if 0 <= nx < rows and 0 <= ny < cols:
                    curr.append(lines[nx][ny])
                if ''.join(curr) == word or ''.join(curr) == word[::-1]:  # Kiểm tra xem có từ cần tìm không
                    good += 1
            if good == 2:  # Nếu tìm được 2 từ thì tăng biến đếm
                count += 1
print(count)
