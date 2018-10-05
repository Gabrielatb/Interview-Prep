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

print isStrobogrammatic('00')