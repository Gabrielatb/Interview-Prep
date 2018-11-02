import heapq 

class KthLargest(object):
# Time: O(nlogk)
# Space: O(k)

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

        # temp = heapified_nums[-3:]
        # self.nums = temp
        # print self.nums
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """


        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        elif val > self.heap[0]:
            heapq.heapreaplace(self.heap, val)

        return self.heap[0]

if __name__ == '__main__':
    lst = KthLargest(3, [4, 5, 8, 2])
    print lst.add(100)

