#!/usr/bin/python3

# valid sudoku board generator
# quick, dirty, but works

import argparse
import oku
import utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-d", "--difficulty", type=str, help="difficulty level")
    parser.add_argument("-r", "--remove", type=int, help="number of answers to remove", default=0)
    parser.add_argument("-o", "--save", type=str, help="grid save filename")
    parser.add_argument("-s", "--solve", type=str, help="filename of grid to solve")
    parser.add_argument("-p", "--print", action="store_true", help="print actual grid to the screen", default=False)
    

    args = parser.parse_args()
    remove = args.remove
    if args.difficulty:
        if args.difficulty == "easy":
            remove = 10
        elif args.difficulty == "medium":
            remove = 13
        elif args.difficulty == "hard":
            remove = 16
        else:
            print("invalid difficulty level.")
            exit(1)
    
    if args.solve is None:
        puzzle = oku.sudoku()
    else:
        puzzle = utils.load(args.solve)
        puzzle.lock()
        
    puzzle.fill_blanks()
    
    puzzle.remove(remove)
    
    if args.save:
        utils.save(puzzle, args.save)
    
    if args.print:
        utils.gprint(puzzle.grid)
