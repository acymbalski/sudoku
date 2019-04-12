
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
        self.lock = False

    def __str__(self):
        return str(self.val)

class sudoku():

    def __init__(self):
        self.grid = self.init_grid()
        
    def init_grid(self):
        # initialize grid with cells
        grid = []
        for r in range(9):
            grid.append([])
            for c in range(9):
                z = cell()
                grid[r].append(z)
                
        return grid


    # get neighbors; horizontal, vertical, and same-square
    def get_neighbors(self, x, y):
        lisNeighbors = []
        
        # horiz
        for r in range(0, 9):
            lisNeighbors.append(self.grid[r][y].val)
        
        # vert
        for c in range(0, 9):
            lisNeighbors.append(self.grid[x][c].val)
            
        # square
        sq_x = int(x / 3)
        sq_y = int(y / 3)
        for r in range(0, 3):
            for c in range(0, 3):
                lisNeighbors.append(self.grid[sq_x * 3 + r][sq_y * 3 + c].val)
                
        # clean list
        n_lis = []
        for itm in lisNeighbors:
            if itm != 0:
                if not itm in n_lis:
                    n_lis.append(itm)
        
        return n_lis


    # get valid values for given x, y cell
    def get_valid(self, x, y):
        lisNeighbors = self.get_neighbors(x, y)
        lisValid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for itm in lisNeighbors:
            if itm in lisValid:
                lisValid.remove(itm)
                
        return lisValid
        
    def fill_blanks(self):
        # keep track of a simple 1-81 index of where we are
        # this makes decrementing a bit simpler when we need
        # to backtrack
        index = 0

        while index < 9 * 9:

            c = index % 9
            r = int(index / 9)

            # if this cell has a value, move on
            # (this can happen if we're solving a partially-filled puzzle)
            if self.grid[r][c].val in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                index += 1
                continue

            # new cell; check for valid neighbors
            if not self.grid[r][c].visited:
                self.grid[r][c].valid = self.get_valid(r, c)
                self.grid[r][c].visited = True
                
            # if there are no valid values, remove this value
            # then go back one and invalidate that value since it
            # leads to an unsolveable state
            if len(self.grid[r][c].valid) == 0:
                # this cell's possibilities must be
                # recalculated after we go back one
                self.grid[r][c].visited = False
                
                # decrement index, remove value of the cell
                # that lead to this unsolveable state
                index -= 1
                
                c = index % 9
                r = int(index / 9)
                
                # iterate backwards until we find a piece that doesn't have a lock on it
                while self.grid[r][c].lock:
                    index -= 1
                    
                    c = index % 9
                    r = int(index / 9)
                    
                
                self.grid[r][c].valid.remove(self.grid[r][c].val)
                self.grid[r][c].val = 0
                
            # we have at least one valid value
            # pick from valid values at random
            else:
                self.grid[r][c].val = random.choice(self.grid[r][c].valid)
                index += 1
                
    def remove(self, amt):
        rem_amt = amt
        while rem_amt > 0:
            # get random x, y
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            
            # don't remove a part that has already been removed
            while self.grid[x][y].val == ' ':
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                
            # if value in cell, hide
            self.grid[x][y].val = ' '
            
            # decrement amt to hide
            rem_amt -= 1
            
    def lock(self):
        # lock all existing numbers from being changed again
        for r in range(9):
            for c in range(9):
                if not self.grid[r][c].val == ' ':
                    self.grid[r][c].lock = True
