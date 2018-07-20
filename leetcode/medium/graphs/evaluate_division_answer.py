    def calcEquation(self, equations, values, queries):
        edges, paths, weights, res = collections.defaultdict(list), {}, {}, []
        for i, e in enumerate(equations): # Generating Graph with "weights"
            edges[e[0]].append(e[1])
            edges[e[1]].append(e[0])
            weights[(e[0], e[1])] = values[i]
            weights[(e[1], e[0])] = 1.0/values[i]
        for e in edges:
            paths[(e,e)] = 1.0 # path to self = 1.0
            queue = collections.deque([(e,1.0)])
            while queue:
                nxt, c = queue.popleft()
                for v in edges[nxt]:
                    if (e, v) not in paths: # enqueue node only if it hasn't been visited yet
                        comp = c * weights[(nxt,v)]
                        paths[(e,v)] = comp 
                        queue.append((v, comp))
        for q in queries:
            res.append(paths.get((q[0], q[1]), -1.0))
        return res