from heapq import heappush, heappop, heapreplace, heapify

# Time: O(n**2)
# Space: O(1)

def insertion_sort(nums):

    for i in range(1, len(nums)):
        key=nums[i]
        j = i-1
        while j>=0 and key<nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    return nums


# Time: O(nlogn)
# Space: O(n)
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
   

        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        self.nums.append(num)
        self.nums.sort()


    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.nums)
        indx = length / 2
        if length % 2 == 0:
            return (self.nums[indx] + self.nums[indx-1]) / 2.0
        else:
            return self.nums[indx] * 1.0
 





# class MedianFinder(object):

#     def __init__(self):
#         #keep smaller half (size >= 1)
#         self.array = []
#         self.length = 0

#     def addNum(self, num):
#         heappush(self.maxHeap, -num)
#         heappush(self.minHeap, -heappop(self.maxHeap))
#         if len(self.minHeap) > len(self.maxHeap):
#             heappush(self.maxHeap, -heappop(self.minHeap))
            

#     def findMedian(self):
#         if len(self.maxHeap) > len(self.minHeap):
#             return float(-self.maxHeap[0])
#         return ((-self.maxHeap[0] + self.minHeap[0] + 0.00 )/2)

if __name__ == '__main__':

    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    # print mf.findMedian()
    mf.addNum(3)
    print mf.findMedian()





