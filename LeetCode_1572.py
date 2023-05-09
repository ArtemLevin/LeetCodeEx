# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and
# all the elements on the secondary diagonal that are not part of the primary diagonal.

import random
# n = random.randint(1, 10)
# matrix = [[random.randint(1, 10) for _ in range(n)] for i in range(n)]
#
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for x in matrix:
    for y in x:
        print(f"{y:^3}", end=' ')
    print("")


i = 0
sumOfDiag = 0
while i < len(matrix[0]):
    sumOfDiag += matrix[i][i] + matrix[len(matrix[0])-1-i][i]
    i+=1
    print(sumOfDiag, end=' ')
if len(matrix[0]) % 2 != 0:
    sumOfDiag = sumOfDiag- matrix[len(matrix[0])//2][len(matrix[0])//2]
print (sumOfDiag)
