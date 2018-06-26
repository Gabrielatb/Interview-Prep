# Award Budget Cuts
# The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem 
# they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks,
#  the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they’d
#   like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher
#    than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

# # Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most 
# efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met 
# (i.e. sum of the N reallocated grants equals to newBudget).

# Analyze the time and space complexities of your solution.

# Example:

# input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

# output: 47 # and given this cap the new grants array would be
#            # [2, 47, 47, 47, 47]. Notice that the sum of the
#            # new grants is indeed 190
# Constraints:

# [time limit] 5000ms

# [input] array.double grantsArray

# 0 ≤ grantsArray.length ≤ 20
# 0 ≤ grantsArray[i]
# [input] double newBudget

# [output] double

def find_grants_cap(grantsArray, newBudget):
    # sort the array in a descending order.
    grantsArray.sort(reverse=True)

    # pad the array with a zero at the end to
    # cover the case where 0 <= cap <= grantsArray[i]
    grantsArray.append(0)


    # calculate the total amount we need to
    # cut back to meet the reduced budget
    surplus = sum(grantsArray) - newBudget


    if surplus <= 0:
        return grantsArray[0]

    for i in range(len(grantsArray)):
        surplus -= (i+1) * (grantsArray[i] - grantsArray[i+1])
        if surplus <= 0:
            return grantsArray[i+1] + (-surplus / float(i+1))
        else:
            continue




print find_grants_cap([2, 100, 50, 120, 1000], 190)
print find_grants_cap([2,4,6], 3)
print find_grants_cap([2,100,50,120,167], 400)
print find_grants_cap([2,100,50,120,1000], 190)
print find_grants_cap([21,100,50,120,130,110], 140)
print find_grants_cap(210,200,150,193,130,110,209,342,117], 1530)

if __name__ == '__main__':
