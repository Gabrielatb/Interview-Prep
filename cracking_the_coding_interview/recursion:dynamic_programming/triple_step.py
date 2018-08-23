###8.1###

#counting the number of ways to get to the top of the stairs


##HOW TO MAKE THE PROBLEM BETTER####
#make more efficient 


###With memoiozation####
def count_steps(n, memo):

    if n in memo:
        return memo[n]

    else:
        memo[n] = count_steps(n-1, memo) + count_steps(n-2, memo) + count_steps(n-3, memo)
        return memo[n]


def climb_stairs(n):
    memo = {}
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3
    return count_steps(n, memo)



# def count_steps(n, memo):

#     if n == 1:
#         return 1
#     elif n==2:
#         return 2
#     elif n ==3:
#         return 3
#     else:
#         steps = count_steps(n-1, memo) + count_steps(n-2, memo) + count_steps(n-3, memo)

#         return steps



























# def countWays(self, n, memo):

#     if n in memo:
#         return memo[n]

#     else:
#         steps = self.countWays(n-1, memo) + self.countWays(n-2, memo) + self.countWays(n-3, memo)
#         memo[n] = steps
#         return steps



# def climbStairs(self, n):

#     memo = {}
#     memo[1] = 1
#     memo[2] = 2
#     memo[3] = 3
#     return self.countWays(n, memo)

