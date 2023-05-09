# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


import random

# sudokuList = [[random.randint(1, 10) for _ in range(1, 10)] for _ in range(1, 10)]
sudokuList = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],
              ["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],
              ["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],
              [".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."]]
for x in sudokuList:
    for y in x:
        print(f"{y:^5}", end='')
    print()

def transposition(grid):
    new_grid = []
    new_two_dim_grid = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            new_grid.append(grid[j][i])
        new_two_dim_grid.append(new_grid[:])
        new_grid = []
    return new_two_dim_grid

def square_3(grid):
    k, t = 0, 0
    square_grids = []
    while k <= 6:
        new_first_grid = []
        new_second_grid = []
        new_third_grid = []
        for i in range(3):
            for j in range(3):
                new_first_grid.append(grid[k+i][j])
                new_second_grid.append(grid[k+i][3+j])
                new_third_grid.append(grid[k+i][6+j])

        square_grids.append(new_first_grid)
        square_grids.append(new_second_grid)
        square_grids.append(new_third_grid)

        k += 3

    return square_grids


def isSudoku(sudokuList):
    for x in sudokuList:
        counter = 1
        for y in x:
            if y != '.': counter+=1
        print(counter, len(set(x)))
        if len(set(x)) != counter: return False
    else: return True


def solvation(array_1, array_2, array_3):
    if bool(isSudoku(array_1)) == True and bool(isSudoku(array_2)) == True and bool(isSudoku(array_3)) == True: return True
    else: return False


print(isSudoku(sudokuList))
print(isSudoku(transposition(sudokuList)))
print(isSudoku(square_3(sudokuList)))


