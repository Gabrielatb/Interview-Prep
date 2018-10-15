# Given a value V, if we want to make change for V Rs, and we have infinite supply
# of each of the denominations in Indian currency, i.e., we have infinite
# supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes,
# what is the minimum number of coins and/or notes needed to make the change?

# Input: V = 70
# Output: 2
# We need a 50 Rs note and a 20 Rs note.

# Input: V = 121
# Output: 3
# We need a 100 Rs note, a 20 Rs note and a
# 1 Rs coin.

#[ 1, 2, 5, 10, 20, 50, 100, 500, 1000 ]

#Time: O(V)
#Space: O(1)

def min_num(lst, V):
   

    count = 0
    i = -1
    while i >= -(len(lst)):
        if lst[i] > V:
            i -= 1
        elif V - lst[i] == 0:
            count += 1
            V -= lst[i]
            break
        elif V - lst[i] > 0:
            V -= lst[i] 
            count += 1

    return count




lst = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
V = 121
print min_num(lst, V)




