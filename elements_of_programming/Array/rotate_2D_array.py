#rotate matrix 90 degress


#Time: O(n)
#Space: O(n)
# def rotate_matrix_90(matrix):
#     return_matrix = []


#     col_indx = 0
#     while col_indx < len(matrix):
#         temp = [0] * len(matrix)
#         for row_indx in reversed(range(len(matrix))):
#             temp[3-row_indx] = matrix[row_indx][col_indx]
#         return_matrix.append(temp)
#         col_indx += 1

#     print return_matrix


# time: O(n**2)
# space: O(1)
def rotate_matrix_90(matrix):
    matrix_length = len(matrix) -1

    for i in range(len(matrix)/2):
        for j in range(i, matrix_length-i):
            print 'this is i: ', i, 'this is j: ', j
            (matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i]) = (matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j])
    return matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print rotate_matrix_90(matrix)
# print print_matrix(matrix)



