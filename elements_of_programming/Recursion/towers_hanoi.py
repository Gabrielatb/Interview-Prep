

# Recursive Python function to solve tower of hanoi 

# Time Complexity: O(2**n) 
# Space Complexity: O(1)

def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 

    if n == 1:
        return 

    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

print TowerOfHanoi('A', 'C', 'B')

































# n = 3
# TowerOfHanoi(n, 'A', 'B', 'C')  