# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

 

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


#unfinished


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """


    indx1 = 0
    indx2 = 0
        
    while len(nums2) >0 and indx1 < len(nums1):
        elem2 = nums2[indx2]
        elem1 = nums1[indx1]
        if elem1 > elem2:
            elem2 = nums2.pop(0)
            nums1.insert(indx1, elem2)
            if len(nums2) == 0:
                break
            indx2 +=1
        indx1 +=1   
    print nums1



    

    # for indx, elem1 in enumerate(nums1):
    #     elem2 = nums2[0]
    #     if elem1 > elem2:
    #         elem2 = nums2.pop(0)
    #         nums1.insert(indx, elem2)


    # if len(nums2) > 0:
    #     for num in nums2:
    #         nums1.append(num)

    # print nums1
    # indx = len(nums1) / 2
    # if len(nums1) % 2 !=0 :
    #     return nums1[indx]
    # else:
    #     return nums1[indx-1], nums1[indx]


print(findMedianSortedArrays([1,3], [2,4]))
