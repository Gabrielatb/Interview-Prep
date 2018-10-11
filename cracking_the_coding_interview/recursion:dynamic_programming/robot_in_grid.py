
# def get_path(maze, row=None, col=None):
#     global total
#     total += 1
#     # print(f"current row={row} col={col}")

#     if row is None and col is None:
#         row = len(maze) - 1
#         col = len(maze[0]) - 1
#         return get_path(maze, row, col)

#     # print(f"current val={maze[row][col]}")

#     point = (row, col)

#     if row < 0 or col < 0 or maze[row][col] is False:
#         return False

#     if row == 0 and col == 0:
#         return [(0, 0)]

#     up_path = get_path(maze, row-1, col)
#     left_path = get_path(maze, row, col-1)

#     if up_path:
#         return up_path + [point]
#     elif left_path:
#         return left_path + [point]

#     return False


def better_get_path(maze, row=None, col=None, failed_points=None):
    global total
    total += 1
    # print(f"current row={row} col={col}")

    if row is None and col is None and failed_points is None:
        return better_get_path(maze, len(maze)-1, len(maze[0])-1, set())

    # print(f"current val={maze[row][col]}")

    point = (row, col)
    # print(f"failed points={failed_points}")

    if point in failed_points:
        # print(f"Already saw {point}")
        return False

    if row < 0 or col < 0 or maze[row][col] is False:
        # print(f"Adding {point} to set")
        failed_points.add(point)
        return False

    if row == 0 and col == 0:
        return [(0, 0)]

    up_path = better_get_path(maze, row-1, col, failed_points)
    left_path = better_get_path(maze, row, col-1, failed_points)

    if up_path:
        return up_path + [point]
    elif left_path:
        return left_path + [point]

    failed_points.add(point)
    return False


total = 0
print("Printing invalid:")
print(get_path(invalid))
print(f"Total hops: {total}")
total = 0
print("Printing valid:")
print(get_path(valid))
print(f"Total hops: {total}")

total = 0
print("Printing better invalid:")
print(better_get_path(invalid))
print(f"Total hops: {total}")
total = 0
print("Printing better valid:")
print(better_get_path(valid))
print(f"Total hops: {total}")