# Grid Illumination: Given an NxN grid with an array of lamp  coordinates.
# Each lamp provides illumination to every square on their x axis,
# every square on their y axis, and every square that lies in their diagonal
# (think of a Queen in chess). Given an array of query coordinates, determine whether
# that point is illuminated or not. The catch is when checking a query all lamps adjacent
# to, or on, that query get turned off. The ranges for the
#  variables/arrays were about:
#   10^3 < N < 10^9, 10^3 < lamps < 10^9, 10^3 < queries < 10^9.