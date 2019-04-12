
import pickle

def gprint(grid):
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

def save(puzzle, filename):
    try:
        pickle.dump(puzzle, open(filename, "wb"))
    except:
        print("Error saving puzzle to {}".format(filename))

def load(filename):
    try:
        return pickle.load(open(filename, "rb"))
    except:
        print("Error loading {}".format(filename))
        return None
