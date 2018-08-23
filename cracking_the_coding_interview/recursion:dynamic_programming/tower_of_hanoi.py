


#Three different disks



# |   |   |
# |   |   |

# A   B   C

# def towers_of_hanoi(n, from_rod, to_rod, aux_rod):

#     if n == 1:
#         print "moving disk from {} to {}".format(from_rod, to_rod)
#         return 


#     towers_of_hanoi(n-1, from_rod, aux_rod, to_rod)
#     print "moving disk from {} to {}".format(from_rod, to_rod)
#     towers_of_hanoi(n-1, aux_rod, to_rod, from_rod)


# towers_of_hanoi(3, 'A', 'C', 'B')


NUM_PEGS = 3


def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg,
                                  use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg,
                                      to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg,
                                      from_peg)

    # Initialize pegs.
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]
    print pegs
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result




