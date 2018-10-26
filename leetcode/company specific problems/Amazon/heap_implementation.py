from heapq import heappush, heappop, heapify  

# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining heap invarient 
# heapify - transform list into heap, in place, in linear time 

#binary heap is binary tree which is complete, except last level all levels
#are strictly filled 
class MinHeap(object):
    def __init__(self):
        self.heap = []

    Time Complexity: O(1)
    def parent(self, indx):
        """ 
        Parent will be middle
        index 
        """

        return indx/2

     # Time Complexity: O(Logn) because if new key is less than parent
     #need to heapify 
    def insert(self, key):
        """
        Insert New key
        """
        heappush(self.heap, k)

     # Time Complexity: O(Logn)
     #if key is less than parent than we need to heapify 
    def decreaseKey(self, indx, new_value):
        """
        Decrease vale of key at index 'indx' to 
        new_val, new_val is smaller than heap[indx]
        """

        self.heap[i] = new_val
        while indx != 0 and self.parent(i) > self.heap[i]:
            #swap self.parent(i) with self.heap[i]
            self.heap[i] , self.heap[self.parent(i)] = ( 
            self.heap[self.parent(i)], self.heap[i]) 

    # Time Complexity: O(Logn) because needs to maintain heap property 
    #therefore need to heapify
    def extractMin(self):
        """
        Removing min value in heap
        """

        return heappop(self.heap)

    # Time Complexity: O(logn)
    def deleteKey(self, indx):
        """
        Function deletes key at indx i
        Makes key negative infinity 
        then extract min value
        """
        self.decreateKey(indx, float('-inf'))
        self.extractMin


    # Time Complexity: O(1)
    def getMin(self):
        """
        returns min value in a heap
        """
        return self.heap[0]




