# given a list of projects, and list of dependencies, (list of pairs of projects

# where the second project is dependent on the first project)

#all project dependencies but be built before the project is , find a build order



#projects: a, b, c, d, e, f 
#dependencies (a,d), (f,b), (b,d), (f,a), (d,c)



def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    #similar to finding a cycle



    graph = {}
    in_degrees = {}
        
    for i in xrange(numCourses):
        graph[i] = []
        in_degrees[i] = 0
    for c,p in prerequisites:
        graph[p].append(c)
        in_degrees[c] += 1
    print in_degrees, graph
    
    # do a bfs/topological sort to cover all courses
    curr_courses = [i for i in xrange(numCourses) if in_degrees[i] == 0]
    courses_taken = 0
    while curr_courses:
        curr_course = curr_courses.pop(0)
        courses_taken += 1
        for next_course in graph[curr_course]:
            in_degrees[next_course] -= 1
            if in_degrees[next_course] == 0:
                curr_courses.append(next_course)
    
    return courses_taken == numCourses

print canFinish(2, [[1,0]])







#output f,e,a,b,d,c
# class Node(object):
#     def __init__(self, data, adjacent=set()):
#         self.data = data
#         self.adjacent = adjacent

# class Graph(object):
#     def __init__(self):

#         self.nodes=set()

#     def add(self, node):

#         self.nodes.add(node)

#     def set_nodes(self, node1, node2):

#         node1.ajacent.add(node2)
#         node2.adjacent.add(node1)



# if __name__ == "__main__":
#     graph =Graph()

