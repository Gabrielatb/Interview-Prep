# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# Example:

# Input:  n = 2
# Output: ["11","69","88","96"]


def findStrobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    

    def isStrobogrammatic(num):
        
        lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    
        strub = ''
        for n in num:
            if n not in lookup:
                return False
            else:
                strub += lookup[n]

        if strub[::-1] == num:
            return num

        return False
    
    if n == 1:
        a = '0'
        b = '9'
    else:
        a = '1'
        b = '9'
    
        while n > 1:
            a += '0'
            b += '9'
            n-=1
        
    return_lst = []
    for i in range(int(a),int(b)+1):
        result = isStrobogrammatic(str(i))
        if result != False:
            return_lst.append(result)
        
    return return_lst

print findStrobogrammatic(4)
            
            
            