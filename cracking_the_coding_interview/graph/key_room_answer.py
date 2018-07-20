Intuition and Algorithm

When visiting a room for the first time, look at all the keys in that room. For any key that hasn't been used yet, add it to the todo list (stack) for it to be used.

See the comments of the code for more details.

class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room








Complexity Analysis

Time Complexity: O(N + E)O(N+E), where NN is the number of rooms, and EE is the total number of keys.

Space Complexity: O(N)O(N) in additional space complexity, to store stack and seen.