#Given String '-^_\n-_-'

def matrix(string):
    matrix = []
    inner_matrix = []
    for char in string:
        if char == '\n':
            matrix.append(inner_matrix)
            inner_matrix = []
        else:
            inner_matrix.append(char)

    matrix.append(inner_matrix)
    return matrix

def get_path(matrix, row, col, mountains):

    point = (row, col)

    if point in mountains:
        return False

    if row < 0 or col < 0 or matrix[row][col] == False or matrix[row][col]=='^':
        mountains.add(point)
        return False

    if row == 0 and col ==0:
        # count +=1 
        return 1

    up_path = get_path(matrix, row - 1, col, mountains)
    left_path = get_path(matrix, row, col-1 , mountains)



    if up_path:
        print 'this is row, col: ', row - 1, col 
        print 'this is up_path: ', up_path
        return up_path + 1
    elif left_path:
        print 'this is row, col: ', row, col-1 
        print 'this is left_path', left_path
        
        return left_path + 1

    mountains.add(point)
    return False

def shortest_path(coor1, coor2, matrix):
    return get_path(matrix, len(matrix)-1, len(matrix[0])-1, set())
    



print shortest_path((0,0), (1,2),matrix('-^_\n-_-'))
# print matrix('-^_\n-_-')