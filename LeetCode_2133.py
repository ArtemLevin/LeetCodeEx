# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

# import random
# n = random.randint(1, 10)
# grid = [[random.randint(1, n) for _ in range(n)] for i in range(n)]
#

def printArray(array):
    for x in grid:
        for y in x:
            print(f"{y:^3}", end=' ')
        print("")


grid = [[1,2,3],[3,1,2],[2,3,1]]


new_grid=[]
new_two_dim_grid=[]
for i in range(len(grid)):
    for j in range (len(grid)):
        new_grid.append(grid[j][i])
    new_two_dim_grid.append(new_grid[:])
    new_grid = []
print(new_two_dim_grid)


# printArray(new_grid)

def isEmpty(grid):
    mySet = set(list(i for i in range(1,len(grid)+1)))
    for x in grid:
        if bool(mySet - set(x)): return True
    return False
print(isEmpty(grid))
print(isEmpty(new_two_dim_grid))
if (isEmpty(grid) == False and isEmpty(new_two_dim_grid) == False): print (True)
else: print(False)
