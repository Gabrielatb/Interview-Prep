# #merge sort implementation from my code school



# if given

#[5,99,7,1,15]

def merge(l, r, nums):
    print 'print inside merge'
    print 'this is l ', l
    print 'this is r ', r
    l_indx = 0
    r_indx = 0
    lst_indx = 0
    length_l = len(l) 
    length_r = len(r)

    while length_l > l_indx and length_r > r_indx:
        if l[l_indx] > r[r_indx]:
            nums[lst_indx] = r[r_indx]
            r_indx +=1
        else:
            nums[lst_indx] = l[l_indx]
            l_indx +=1
        lst_indx +=1
    print 'print nums for first time ', nums


    while length_l > l_indx:
        print 'inside l'
        nums[lst_indx] = l[l_indx]
        l_indx +=1
        lst_indx +=1


    while length_r > r_indx:
        print 'inside r'
        nums[lst_indx] = r[r_indx]
        r_indx +=1
        lst_indx +=1

    print 'this is nums ', nums
    return nums

def merge_lst(lst):

    if len(lst) < 2:
        return lst

    mid = len(lst) / 2
    print mid

    left = lst[:mid]
    print 'this is left ', left
    right = lst[mid:]
    print 'this is right ', right

    merge_lst(left)
    # print 'this is l ' , l
    merge_lst(right)
    # print 'this is r ', r
    merge(left, right, lst)

    return lst

print merge_lst([99, 5,7,1,15])
