#if there are three types of edits, insert, delete replace given two strings
#write a function to check if they are one edit, zero edits away


def one_away(str1, str2):

    lst1 = list(str1)
    lst2 = list(str2)

    if len(lst1) == len(lst2):
        if lst1 == lst2:
            return True
        edit = 0
        for char in lst1:
            if char in lst2:
                lst2.remove(char)
            else:
                edit +=1
        if edit > 1:
            return False
        return True

    if abs(len(lst1) - len(lst2)) == 1:
        max_lst = max(lst1, lst2)
        min_lst = min(lst1, lst2)
        edit = 0
        for char in max_lst:
            if char in min_lst:
                max_lst.remove(char)
            else:
                edit +=1
        if edit > 1:
            return False
        return True

    return False














print one_away('pale', 'ple')
print one_away('pales', 'pale')
print one_away('pale', 'bale')
print one_away('pale', 'bake')
print one_away('pale', 'pale')
