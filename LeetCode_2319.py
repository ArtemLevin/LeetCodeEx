# A square matrix is said to be an X-Matrix if both of the following conditions hold:
#
# All the elements in the diagonals of the matrix are non-zero.
# All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square matrix,
# return true if grid is an X-Matrix. Otherwise, return false.

import random
n = random.randint(5, 8)
grid = [[random.randint(1, 10) for _ in range(n)] for i in range(n)]

for x in grid:
    for y in x:
        print(f"{y:^3}", end=' ')
    print("")
def isX(grid):
    length = len(grid[0])
    for i in range(length):
        for j in range(length):
            if i == j or i == length - 1 - j:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True
print(isX(grid))

def toOneDimArray(grid):
    oneDimArray = []
    length = len(grid[0])
    for i in range(length):
        for j in range(length):
            if i == j or i == length - 1 - j:
                oneDimArray.append(0)
            else:
                oneDimArray.append(grid[i][j])
    return oneDimArray
print(toOneDimArray(grid))