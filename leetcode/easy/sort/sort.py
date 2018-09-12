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

#1.2.3
#4.11.6
#sorted_lst = [1.2.3, ]
    
def bubble_sort(lst):
    
    # sorted_list = []
    
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


    # def _sort(self, arr):
    #     arr1 = []
    #     arr2 = []

    #     n = len(arr)

    #     if n <= 1:
    #         return

    #     for i in range(0, n):
    #         if i < (n / 2):
    #             arr1.append(arr[i])
    #         else:
    #             arr2.append(arr[i])

    #     self._sort(arr1)
    #     self._sort(arr2)
    #     self._merge(arr, arr1, arr2)
    #     return arr

    # def _merge(self, arr, arr1, arr2):  
    #     end1 = len(arr1)
    #     end2 = len(arr2)
    #     start1 = 0
    #     start2 = 0
    #     k = 0

    #     while (start1 < end1) and (start2 < end2):
    #         if arr1[start1] < arr2[start2]:
    #             arr[k] = arr1[start1]
    #             start1 += 1
    #         else:
    #             arr[k] = arr2[start2]
    #             start2 += 1
    #         k += 1

    #     while start1 < end1:
    #         arr[k] = arr1[start1]
    #         start1 += 1
    #         k += 1

    #     while start2 < end2:
    #         arr[k] = arr2[start2]
    #         start2 += 1
    #         k += 1

print sort([ '1.2.3', '4.11.6', '4.2.0',
        '1.5.19',
        '1.5.5',
        '4.1.3',
        '2.3.1',
        '10.5.5',
        '11.3.0'])
   