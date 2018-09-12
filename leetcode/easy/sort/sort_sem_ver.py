# Enter your code here. Read input from STDIN. Print output to STDOUT
#    definition: 
#        Sem-ver is defined as a software versioning structure, where given a version number MAJOR.MINOR.PATCH, increment the:
#        MAJOR version when you make incompatible API changes,
#        MINOR version when you add functionality in a backwards-compatible manner, and
#        PATCH version when you make backwards-compatible bug fixes.
#        Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
#
#    questiodn:
#        How do you sort sem-ver values (1.1.1 vs 1.2.1 etc)
#
#    sample input: #array of items  
#        1.2.3
#        4.11.6
#        4.2.0
#        1.5.19
#        1.5.5
#        4.1.3
#        2.3.1
#        10.5.5
#        11.3.0

#output:sorted_array:  1.2.3, 1.5.5, 1.5.19 
#        [1.2.3
#        4.11.6
#        4.2.0
#        1.5.19
#        1.5.5
#        4.1.3
#        2.3.1
#        10.5.5
#        11.3.0]

#My original solution   
#Time complexity O(n**2)
#Space complexity O(1) 
def bubble_sort(lst):
    
    
    for i in range(len(lst)-1):
        for j in range(len(lst)-i):
        
            elem1 = lst[i].split('.')
            elem2 = lst[i+j].split('.')
            
            if int(elem1[0]) > int(elem2[0]):
                temp = lst[i]
                lst[i] = lst[i+j]
                lst[i+j] = temp
                
            elif  int(elem1[0]) == int(elem2[0]):
                if int(elem1[1]) > int(elem2[1]):
                    temp = lst[i]
                    lst[i] = lst[i+j]
                    lst[i+j] = temp
                elif int(elem1[1]) == int(elem2[1]):
                    if int(elem1[2]) > int(elem2[2]):
                        temp = lst[i]
                        lst[i] = lst[i+j]
                        lst[i+j] = temp
            
    print lst

#####################################################
#My Merge Sort solution   
#Time complexity O(nlogn)
#Space complexity O(n) -- I'm adding extra list 
def mergesort(lst):

    length = len(lst)
    left = []
    right = []

    if length < 2:
        return 


    for i in range(0,length):
        if i < length / 2:
            left.append(lst[i])
        else:
            right.append(lst[i])


    mergesort(left)
    mergesort(right)
    merge(left, right, lst)

    return lst

def merge(l, r, nums):
    len_l = len(l)
    len_r = len(r)
    left_indx = 0
    right_indx = 0
    nums_indx = 0

    while len_l > left_indx and len_r > right_indx:
        l_elem = l[left_indx].split('.')
        r_elem = r[right_indx].split('.')
      

        if int(l_elem[0]) > int(r_elem[0]):
            nums[nums_indx] = r[right_indx]
            right_indx += 1
        elif int(l_elem[0]) == int(r_elem[0]):
            if int(l_elem[1]) > int(r_elem[1]):      
                nums[nums_indx] = r[right_indx]
                right_indx += 1
            elif int(r_elem[1]) > int(l_elem[1]):       
                nums[nums_indx] = l[left_indx]
                left_indx += 1
            elif int(l_elem[1]) == int(r_elem[1]):
                if int(l_elem[2]) > int(r_elem[2]):
                    nums[nums_indx] = r[right_indx]
                    right_indx += 1
                elif int(r_elem[2]) > int(l_elem[2]):
                    nums[nums_indx] = l[left_indx]
                    left_indx += 1
        else:
            nums[nums_indx] = l[left_indx]
            left_indx += 1

        nums_indx += 1

        

    while len_l > left_indx:
        nums[nums_indx] = l[left_indx]
        left_indx += 1
        nums_indx += 1

    while len_r > right_indx:
        nums[nums_indx] = r[right_indx]
        right_indx += 1
        nums_indx += 1



print mergesort([ '1.2.3', '4.11.6', '4.2.0',
        '1.5.19',
        '1.5.5',
        '4.1.3',
        '2.3.1',
        '10.5.5',
        '11.3.0'])
   