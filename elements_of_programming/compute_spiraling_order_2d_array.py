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

def spiral_matrix(matrix):
        return_lst = []
        while matrix:
            
            #adding to return lst the first list
           
            return_lst += matrix[0]
            
            #rotating matrix to the left
            matrix = zip(*matrix[1:])[::-1]
            print matrix
            
        # print return_lst
        return return_lst


print spiral_matrix([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])