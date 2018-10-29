#Topological sorting alg

#create graph

class Solution(object):
    def __init__(self):
        self.graph  = {}}
        self.stack = []
        self.visited = []
        self.ans = True
        
    def topological_sort(self, req):
        if self.ans == False:
            return False

        self.visited.append(req)
        if req not in self.graph:
            self.stack.append(req)
            return

        for r in self.graph[req]:

            if r not in self.visited:
                self.topological_sort(r)

            elif r not in self.stack:
                self.ans = False
                return
                  
        self.stack.append(req)
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == []:
            return True
   
        for preq in prerequisites:
            if preq[0] not in self.graph:
                self.graph[preq[0]] = [preq[1]]
            else:
                self.graph[preq[0]].append(preq[1])
            
        for indx in range(numCourses):
            self.visited.append(indx)
            self.topological_sort(indx)
        return self.ans
         
 

if __name__ == '__main__':

    course = Solution()
    print course.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])
                
        




################################################################################
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.adjacency = set()
# class Graph(object):
#     def __init__(self):
#         self.nodes = []


#     def add_nodes(self, nodes):

#         for node in nodes:
#             self.nodes.append(node)


#     def add_edge(self, node1, edge):

#         node1.adjacency.add(edge.data)
    

#     def topological_sort_helper(self, node, visited, stack):
#         #mark node as visited
#         visited.append(node)
#         for n in node.adjacency:
#             if n not in visited:
#                 self.topological_sort_helper(n, visited, stack)

#         stack.append(node.data)


#     def topological_sort(self):

#         #marking all nodes as not having been visited
#         visited = []
#         stack = []

#         for node in self.nodes:
#             if node not in visited:
#                 self.topological_sort_helper(node, visited, stack)
#         return stack





# if __name__ == '__main__':
#     A = Node("A")
#     B = Node("B")
#     C = Node("C")
#     D = Node("D")
#     E = Node("E")
#     F = Node("F")
#     G = Node("G")
#     H = Node("H")
#     I = Node("I")
#     J = Node("J")
   

#     graph= Graph()

#     graph.add_nodes([A, B, C,D, E, F, G, H, I, J])

#     graph.add_edge(A,B)
#     graph.add_edge(A,F)
#     graph.add_edge(B,H)
#     graph.add_edge(D,C)
#     graph.add_edge(D,I)
#     graph.add_edge(D,E)
#     graph.add_edge(E,I)
#     graph.add_edge(G,A)
#     graph.add_edge(G,B)
#     graph.add_edge(G,C)
#     graph.add_edge(I,C)
#     graph.add_edge(J,E)


#     print A.adjacency
#     # print graph.topological_sort()


