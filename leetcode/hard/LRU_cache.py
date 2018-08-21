# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity 
        self.queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if len(self.queue) == 0:
            return -1

        for tup in self.queue:
            if tup[0] == key:
                temp = self.queue[-1]
                self.queue[-1] = self.queue[0]
                self.queue[0] = temp
                return self.queue[-1][1]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if len(self.queue) == 0:
            self.queue.append((key, value))
        
        for indx, tup in enumerate(self.queue):
            if tup[0] == key:
                self.queue[indx] = (key, value)
                return
        
        if len(self.queue) == self.capacity:
            self.queue.pop(0)
        self.queue.append((key, value))


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(2,2)
    # cacheget(1)
    # cache.put(3,3)



# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

# [null,null,null,2,null,null,-1]

