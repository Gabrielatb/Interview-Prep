###8.1###

#counting the number of ways to get to the top of the stairs


##HOW TO MAKE THE PROBLEM BETTER####
#make more efficient 


###With memoization####
# def count_steps(n, memo):

#     if n in memo:
#         return memo[n]

#     else:
#         memo[n] = count_steps(n-1, memo) + count_steps(n-2, memo) + count_steps(n-3, memo)
#         return memo[n]


# def climb_stairs(n):
#     memo = {}
#     memo[1] = 1
#     memo[2] = 2
#     memo[3] = 3
#     return count_steps(n, memo)

#####Without saving values###########

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








#################################################################################


#alternative problem, consider we can only take 1, 3, 5 steps represented in a set (1,3,5)


def count(n, steps, memo):

    if n == 0:
        return 1

    total = 0

    for i in steps:

        if n-1 >=0:

            total+= count(n-i, steps)



    return total




















