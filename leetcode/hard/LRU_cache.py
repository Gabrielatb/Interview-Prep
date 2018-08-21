# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.q = []
        self.timestamp = 0

    def get(self, key):
        if key not in self.cache:
            return -1
            
        item = self.cache[key]
        item[1] = self.timestamp
        self.q.append((self.timestamp, key))
        
        self.timestamp += 1
        
        return item[0]
        

    def put(self, key, value):
        
        if key not in self.cache and len(self.cache) >= self.capacity:
            while True:
                t, k = self.q.pop(0)
                if self.cache[k][1] == t:
                    break
            self.cache.pop(k)
                
        self.cache[key] = [value, self.timestamp]
        self.q.append((self.timestamp, key))        
            
        self.timestamp += 1



if __name__ == '__main__':
    cache = LRUCache(2)
    # cache.put(2,1)
    # cache.put(2,2)
    # cache.get(2)
    # cache.put(1,1)
    # cache.put(4,1)
    # cache.get(2)



# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

# [null,null,null,2,null,null,-1]

