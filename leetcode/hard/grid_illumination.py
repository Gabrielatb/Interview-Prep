# Grid Illumination: Given an NxN grid with an array of lamp  coordinates.
# Each lamp provides illumination to every square on their x axis,
# every square on their y axis, and every square that lies in their diagonal
# (think of a Queen in chess). Given an array of query coordinates, determine whether
# that point is illuminated or not. The catch is when checking a query all lamps adjacent
# to, or on, that query get turned off. The ranges for the
#  variables/arrays were about:
#   10^3 < N < 10^9, 10^3 < lamps < 10^9, 10^3 < queries < 10^9.



class GridIllumination(object):
    def __init__(self, n, lamps):
        self.columns =  [n]
        self.rows = [n]
        self.d_left = [(size) * 2 - 2]
        self.d_right = [(size) * 2 - 2]

        for lamp in lamps:
            addLamp(lamp)

    def addLamp(lamp):
        x = lamp[0]
        y = lamp[1]
        columns[x] = True
        rows[y] = True
        d_left[x + y] = True
        d_right[x - y] = True

    def query(x,y):
        if self.columns[x] or self.rows[y] or self.d_left[x+y] or self.d_right[x-y]:
            return True

class GridIlluminationRemove(object):
    def __init__(self, n, lamps):
        self.lamps = lamps
        self.columns =  [n]
        self.rows = [n]
        self.d_left = [(size) * 2 - 2]
        self.d_right = [(size) * 2 - 2]

        for lamp in lamps:
            addLamp(lamp)



        def addLamp(lamp):
            x = lamp[0]
            y = lamp[1]
            columns[x] +=1
            rows[y] +=1
            leftDiagonals[x + y] +=1
            rightDiagonals[x - y] +=1


        def removeLamp(lamp):
            x = lamp[0]
            y = lamp[1]
            columns[x] -=1
            rows[y] -=1
            d_left[x + y] -=1
            d_right[x - y] -=1
            lamps.remove(lamp)
 

        def query(x, y):
            neighbors = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x, y], [x + 1, y], [x - 1, y + 1], [x , y + 1], [x + 1, y + 1]]
            for neighbor in neighbors:
                if neighbor in lamps:
                    removeLamp(neighbor)
            columns[x] > 0 || rows[y] > 0 || leftDiagonals[x + y] > 0 || rightDiagonals[x - y] > 0
 
