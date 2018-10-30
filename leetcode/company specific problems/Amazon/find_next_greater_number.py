# Given a number n find the smallest number that has same set of digits as n and is greater than n.
# If x is the greatest possible number with its set of digits then print not possible.
# Examples:
# For simplicity of implementation, we have considered input number as a string.

# Input:  n = "218765"
# Output: "251678"

# Input:  n = "1234"
# Output: "1243"

# Input: n = "4321"
# Output: "Not Possible"

# Input: n = "534976"
# Output: "536479"


#traverse list from right to left
#swap element whose prev number if greater
#isolate right side of swap, sort in ascending order

def nextGreaterElement(n):
    """
    :type n: int
    :rtype: int
    """


    num_string = str(n)
    num_lst = []
   
    for num in num_string:
        num_lst.append(int(num))


    #find position where prev num is greater
    length = len(num_lst)
    for indx in range(length-1, 0, -1):
        if num_lst[indx] > num_lst[indx-1]:
            break

    #nums in ascending order
    print indx
    if indx-1 == 0:
        return -1

    #finding smallest digit at indx - 1
    x = num_lst[indx-1]
    smallest = indx

    for j in range(indx+1, len(num_lst)):
        if x < num_lst[j] and num_lst[j] < num_lst[smallest]:
            smallest = j


    #swap 

    num_lst[smallest], num_lst[indx-1] = num_lst[indx-1], num_lst[smallest]
    
    return_num_lst = sorted(num_lst[indx:])

    return num_lst[:indx] + return_num_lst

            


# print nextGreaterElement(218765)
# print nextGreaterElement(1234)
# print nextGreaterElement(4321)
# print nextGreaterElement(534976)
print nextGreaterElement(12)
# print nextGreaterElement(230241)

