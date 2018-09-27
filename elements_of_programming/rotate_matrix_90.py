# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]
                

# Time Complexity O(n**2)
# Space Complexity O(1)