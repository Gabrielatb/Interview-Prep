#generic implementation of selection_sort

def selection_sort(lst):

    for i in range(len(lst)):
        high = None
        for j in range(len(lst) - i):
            if high is None or lst[j] > lst[high]:
                high = j

        lst[j], lst[high] = lst[high], lst[j]

#Runtime O(n**2)
#Space O(1)