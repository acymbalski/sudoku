#!/usr/bin/python3

# valid sudoku board generator
# quick, dirty, but works

import random

# cell
# contains a value, a list of possible values,
# and a flag for whether or not we have already
# visited this cell (used for potential backtracking)
class cell():
    def __init__(self):
        self.valid = []
        self.val = 0
        self.visited = False

    def __str__(self):
        return str(self.val)

# initialize grid with cells
grid = []
for r in range(9):
    grid.append([])
    for c in range(9):
        z = cell()
        grid[r].append(z)

# print grid with fencing
def gprint():
    print()
    for r in range(9):
        for c in range(9):
            print(str(grid[r][c]) + ' ', end="")
            if c % 3 == 2 and c != 8:
                print('| ', end="")
        print()
        if r % 3 == 2 and r != 8:
            print(('- ' * 3 + '+ ') * 2 + '- ' * 3)
    print()

# get neighbors; horizontal, vertical, and same-square
def get_neighbors(x, y):
    lisNeighbors = []
    
    # horiz
    for r in range(0, 9):
        lisNeighbors.append(grid[r][y].val)
    
    # vert
    for c in range(0, 9):
        lisNeighbors.append(grid[x][c].val)
        
    # square
    sq_x = int(x / 3)
    sq_y = int(y / 3)
    for r in range(0, 3):
        for c in range(0, 3):
            lisNeighbors.append(grid[sq_x * 3 + r][sq_y * 3 + c].val)
            
    # clean list
    n_lis = []
    for itm in lisNeighbors:
        if itm != 0:
            if not itm in n_lis:
                n_lis.append(itm)
    
    return n_lis

# get valid values for given x, y cell
def get_valid(x, y):
    lisNeighbors = get_neighbors(x, y)
    lisValid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for itm in lisNeighbors:
        if itm in lisValid:
            lisValid.remove(itm)
            
    return lisValid

# keep track of a simple 1-81 index of where we are
# this makes decrementing a bit simpler when we need
# to backtrack
index = 0

while index < 9 * 9:

    c = index % 9
    r = int(index / 9)

    # new cell; check for valid neighbors
    if not grid[r][c].visited:
        grid[r][c].valid = get_valid(r, c)
        grid[r][c].visited = True
        
    # if there are no valid values, remove this value
    # then go back one and invalidate that value since it
    # leads to an unsolveable state
    if len(grid[r][c].valid) == 0:
        # this cell's possibilities must be
        # recalculated after we go back one
        grid[r][c].visited = False
        
        # decrement index, remove value of the cell
        # that lead to this unsolveable state
        index -= 1
        
        c = index % 9
        r = int(index / 9)
        
        grid[r][c].valid.remove(grid[r][c].val)
        grid[r][c].val = 0
        
    # we have at least one valid value
    # pick from valid values at random
    else:
        grid[r][c].val = random.choice(grid[r][c].valid)
        index += 1
    
# print board
gprint()
