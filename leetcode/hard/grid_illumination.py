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
        self.lamps = lamps
        self.columns =  [0]*n #list of size n
        self.rows = [0]*n # list of size n
        self.d_left = [0]*(2*(n-1) + 1) # list of dia
        print self.d_left
        self.d_right = [0]*(2*(n-1) + 1)
 


    def addLamp(self, lamp):
        x = lamp[0]
        y = lamp[1]
        self.columns[x] +=1
        self.rows[y] +=1
        self.d_left[x + y] +=1
        self.d_right[x - y] +=1

    def removeLamp(self, lamp):
        x = lamp[0]
        y = lamp[1]
        self.columns[x] -=1
        self.rows[y] -=1
        self.d_left[x + y] -=1
        self.d_right[x - y] -=1
        lamps.remove(lamp)

        for lamp in self.lamps:
            self.addLamp(lamp)


    def query(self, x, y):
        #             [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x, y], [x + 1, y], [x - 1, y + 1], [x , y + 1], [x + 1, y + 1]]
        # neighbors = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x, y], [x + 1, y], [x - 1, y + 1], [x , y + 1], [x + 1, y + 1]]
        for neighbor in neighbors:
            if neighbor in self.lamps:
                self.removeLamp(neighbor)
        if self.columns[x] or self.rows[y] or self.d_left[x + y]  or self.d_right[x - y]:
            return 1
if __name__ == '__main__':
    lamps = [[0, 0], [4, 4]]
    grid = GridIllumination(5, lamps)
    print "grid", grid.rows,grid.columns
    print "grid 11 result:",grid.query(1,1)
    print "grid 10 result:",grid.query(1,0)
    print "grid 00 result:",grid.query(0,0)
    print "grid 00 result:",grid.query(2,1)

    r = len(grid.rows)
    c = len(grid.columns)
    for i in range(5):
        for j in range(5):
            print grid


