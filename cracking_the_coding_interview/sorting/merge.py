# """This merge sort is written for ease of understanding. An implementation with 
# better runtime is implemented in sorts.py."""


# def merge_sort(lst):
#     """Merge sort list and return result."""

#     print("calling merge_sort on", lst)

#     # Break everything down into a list of one
#     if len(lst) < 2:  # if length of lst is 1, return lst
#         print("returning", lst)
#         return lst

#     mid = int(len(lst) / 2)  # index at half the list
#     lst1 = merge_sort(lst[:mid])  # divide list in half
#     lst2 = merge_sort(lst[mid:])  # assign other half

#     return make_merge(lst1, lst2)


# def make_merge(lst1, lst2):
#     """Merge lists."""

#     # Compare first items of each pair of lists & interleave
#     result_list = []
#     print(lst1, lst2)
#     while len(lst1) > 0 or len(lst2) > 0:
#         # if items left in both lists
#         # compare first items of each list
#         if lst1 == []:
#             result_list.append(lst2.pop(0))
#         elif lst2 == []:
#             result_list.append(lst1.pop(0))
#         elif lst1[0] < lst2[0]:
#             # append and rm first item of lst1
#             result_list.append(lst1.pop(0))
#         else:
#             # append and rm first item of lst2
#             result_list.append(lst2.pop(0))

#     print("returning merge", result_list)
#     return result_list



def merge_sort(lst):
    """Merge sort.

    Divide and conquer: reduce to lists of 0-1 items, then recombine.

    Runtime: O(n log n)
    """
    print lst
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge-lecture-snippet-start
        left_index = right_index = new_index = 0

        # Interleave left and right into list

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1
        # merge-lecture-snippet-end

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1

        return lst

if __name__ == "__main__":
    print(merge_sort([2, 1, 7, 4]))
