def isValid(s):
    valid_parens = {'(': ')', '{': '}', '[': ']'}
    
    end_paren = []
    for char in s:
        if char in valid_parens:
            end_paren.append(valid_parens[char])
        else:
            if len(end_paren) == 0:
                return False
            paren = end_paren.pop()
            if paren != char:
                return False
    
    if len(end_paren) > 0:
        return False
    return True
            