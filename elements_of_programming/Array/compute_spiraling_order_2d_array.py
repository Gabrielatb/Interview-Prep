# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# time: O(n)
# space: O(n)

def spiral_matrix(matrix):

    while matrix:

        for num in matrix[0]:
            print num

        #rotate matrix to the left
        matrix = zip(*matrix[1:])[::-1]


print spiral_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])





















