# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    mult = 1
    total = 0
    for num in digits[::-1]:
        total += num * mult

        mult = mult *10

    total +=1
    total_string = str(total)
    ret = []
    for num_string in total_string:
        ret.append(int(num_string))

    return ret

print plusOne([1,2,3])
print plusOne([9,9])
   




