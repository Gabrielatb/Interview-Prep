###8.1###



def countWays(self, n, memo):

    if n in memo:
        return memo[n]

    else:
        steps = self.countWays(n-1, memo) + self.countWays(n-2, memo) + self.countWays(n-3, memo)
        memo[n] = steps
        return steps



def climbStairs(self, n):

    memo = {}
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3
    return self.countWays(n, memo)

