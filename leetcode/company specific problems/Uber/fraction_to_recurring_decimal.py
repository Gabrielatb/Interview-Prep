# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
# numerator = 1, denominator = 2
# Output: "0.5"

#Input: numerator = 2, denominator = 1
# Output: "2"
   
    num, remainder = divmod(numerator, denominator)
    strng = t = '-' if numerator * denominator < 0 else ''
    fraction = [strng + str(num)]
    if remainder == 0:
        return ''.join(fraction)
    else:
        fraction.append('.')
        dict_ = {}
        while remainder != 0:
            if remainder in dict_:
                


# print fractionToDecimal(0, -5)
# print fractionToDecimal(1, 2)
# print fractionToDecimal(2, 1)
# print fractionToDecimal(2, 3)
print fractionToDecimal(50, 8)
