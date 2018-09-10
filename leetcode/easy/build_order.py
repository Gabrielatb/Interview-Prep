"""
Get Load Order
Given a dictionary of dependencies and a module, write a function that will 
return the load order to run that module.
Example:
A: B, C
B: C, D
C:
D: E, F
E:
F:
load(E) => E
load(F) => F
load(D) => E, F, D OR F, E, D
load(B) => C, E, F, D, B
"""

#iterating through my dictionary, when I reach the module, place dependencies in the 
#load order list
#all the depencies would go in stack


#load_order = [B,C,D]
#queue = 
#

def load_order(dep, m):

    load_order = []
    seen = [m]
    queue = [m]

    while queue:
        module = queue.pop(0)
        load_order.append(module)
        if dep[module] != '':
            for mod in dep[module]:
                if mod not in seen:
                    queue.append(mod)
                    seen.append(mod)

    return load_order[::-1]

dict_ = {'A':['B','C'], 'B': ['C', 'D'], 'C': '', 'D': ['E', 'F'], 'E':'', 'F': ''}
print load_order(dict_, 'E')
print load_order(dict_, 'F')
print load_order(dict_, 'D')
print load_order(dict_, 'B')
