# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# Example:

# Input: low = "50", high = "100"
# Output: 3 
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        def isStrobogrammatic(num):
            """
            :type num: str
            :rtype: bool
            """
            lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}


            strub = ''
            for n in num:
                if n not in lookup:
                    return False
                else:
                    strub += lookup[n]

            if strub[::-1] == num:
                return True

            return False
        
        count = 0
        
        for i in range(int(low), int(high)+1):
            if isStrobogrammatic(str(i)) != False:
                count +=1
                
        return count