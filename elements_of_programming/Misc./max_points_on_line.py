# Given n points on a 2D plane, 
# find the maximum number of points that lie on the same straight line.


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


def num_points(points, point):
    # count_vertical = 0
    # #check vertical: change x, but not y
    # for y in range(len(points)):
    #     temp_point = [point.x, y]
    #     if temp_point in points:
    #         count_vertical +=1

    # #check horizontal
    # count_horizontal = 0
    # for x in range(len(points)):
    #     temp_point = [x, point.y]
    #     if temp_point in points:
    #         count_horizontal +=1
    # #check upper diagonal on left side
    end_point = max(points)
    i=0
    count_right_diagonal = 1
    
    for j in range(len(points)):
        temp_point = [i,j]
        if temp_point <= end_point:
            if temp_point in points:
                count_right_diagonal += 1
        i+=1
    return count_right_diagonal 
print num_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], [3, 2])
    # #check diagonal left_slant
    # count_left_diagonal = 0
    # end_point = max(points)
    # i=len(points) - 1
    # while i >= 0:
    #     for j in reversed(range(len(points))):
    #         temp_point = [i,j]
    #         if temp_point <= end_point:
    #             if temp_point in points:
    #                 count_left_diagonal += 1
    #         i+=1
    # return max(count_left_diagonal,count_right_diagonal,count_horizontal, count_vertical )
        
        
# def maxPoints(self, points):
#     """
#     :type points: List[Point]
#     :rtype: int
#     """
    
#     max_point = 0
#     for point in points:
#         print point
#         max_points= max(self.num_points(points, point), max_point)
#     return max_point