def floodfill(matrix, row, col, new_color, prev_color):
    def recursive(matrix, row, col, prev_color, new_color):
        if row >= len(matrix) or col >= len(matrix[0]) or col < 0 or row < 0:
            return None


        if matrix[row][col] == prev_color:
            matrix[row][col] = new_color

            recursive(matrix, row+1, col, prev_color, new_color)
            recursive(matrix, row-1, col, prev_color, new_color)
            recursive(matrix, row, col+1, prev_color, new_color)
            recursive(matrix, row, col-1, prev_color, new_color)

    prev_color = matrix[row][col]
    recursive(matrix, row, col, prev_color, new_color)
    return matrix



matrix = [[1, 2, 3], [1, 3, 3], [1, 3, 2]]
row = 1
col = 1
new_color = 4
prev_color = matrix[row][col]
print floodfill(matrix, row, col, new_color, prev_color)

