# Given a sorted array of strings that is interspersed with empty strings,
# write a method to find the location of a given string




# '', *l'', 'a', '','b', '', '', 'c', '', ''*r], 'a'

def sparse_search(lst, value, l_index=0, r_index=None):
    """
    >>> i = sparse_search(['', '', 'a', '', 'b', '', '', 'c', '', ''], 'a')
    >>> i == 2
    True
    >>> i = sparse_search(['', '', 'a', '', 'b', '', '', 'c', '', ''], 'c')
    >>> i == 7
    True
    >>> i = sparse_search(['', '', 'a', '', 'b', '', '', 'c', '', ''], 'd')
    >>> i is None
    True
    >>> i = sparse_search(['', '', ''], 'a')
    >>> i is None
    True
    >>> i = sparse_search(['a', 'b', 'c'], 'b')
    >>> i == 1
    True
    """

    if r_index is None:
        r_index = len(lst) - 1

    mid = (l_index+r_index) / 2

    if lst[mid] == '':
        left = mid -1
        right = mid + 1

        while True:
            if left < l_index and right > r_index:
                return None
            elif right <= r_index and lst[right] != '':
                mid = right
                break
            elif left>= l_index and lst[left] != '':
                mid = left
                break
            right +=1
            left -=1

    if lst[mid] == value:
        return mid
    elif lst[mid] < value:
        return sparse_search(lst, value, mid+1, r_index)
    elif lst[mid] > value:
        return sparse_search(lst, value, l_index, mid-1)










# print find_index(["at", "", "", "", "ball", "", ""], value, l=0, r=None)

if __name__ == "__main__":
    import doctest
    doctest.testmod()