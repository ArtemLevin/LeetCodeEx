# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def sum(array):
#
#     if len(array) == 0:
#         return 0
#     else:
#         return array[0] + sum(array[1:])
#
# print(sum(array))

# -------------------------------------------------------------------------------------------------------------------

# TOWEROFHANOI

# import sys
#
# TOTAL_DISKS = 6
# TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS+1))), 'B': [], 'C': []}
#
#
# def printDisk(diskNum):
#     emptySpace = ' '*(TOTAL_DISKS - diskNum)
#     if diskNum == 0:
#         sys.stdout.write(emptySpace + '||' + emptySpace)
#     else:
#         diskspace = '@'*diskNum
#         diskNumLabel = str(diskNum).rjust(2, '_')
#         sys.stdout.write(emptySpace + diskspace + diskNumLabel + diskspace + emptySpace)
#
#
# def printTowers():
#     for level in range(TOTAL_DISKS, -1, -1):
#         for tower in (TOWERS['A'], TOWERS['B'],TOWERS['C']):
#             if level >= len(tower):
#                 printDisk(0)
#
#             else:
#                 printDisk(tower[level])
#         sys.stdout.write('\n')
#     emptySpace = ' '*(TOTAL_DISKS)
#     print('%s A%s%s B%s%s C\n' %(emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))
#
#
# def moveOneDisk(startTower, endTower):
#     disk = TOWERS[startTower].pop()
#     TOWERS[endTower].append(disk)
#
#
# def solve(numberOfDisks, startTower, endTower, tempTower):
#     if numberOfDisks == 1:
#         moveOneDisk(startTower, endTower)
#         printTowers()
#         return
#     else:
#         solve(numberOfDisks - 1, startTower, tempTower, endTower)
#         moveOneDisk(startTower, endTower)
#         printTowers()
#         solve(numberOfDisks - 1, tempTower, endTower, startTower)
#         return
#
#
# printTowers()
# solve(TOTAL_DISKS, 'A', 'B', 'C')

# while True:
#     printTowers()
#     print('Enter letter of start tower and the en tower. (A, B, C) or Q to quit.')
#     move = input().upper()
#     if move == 'Q':
#         sys.exit()
#     elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#         moveOneDisk(move[0], move[1])

# ------------------------------------------------------------------------------------------------------------
# for i in range(5):
#     word = str(i).center(5, '_')
#     print(word)

# --------------------------------------------------------------------------------------------------------------

import random
import time
import timeit

# new_array = list(map(lambda x: '.' if x%2 == 0 else x, [random.randint(0,10) for i in range(10)]))
new_array = ['.', 1, 2, 3, '.', '.', '.', '.', '.', 9]


def fullfillTheArray(new_array):
    for _ in new_array:
        print(_, end='')
    i = 0
    while i < (len(new_array)):
        if new_array[i] == '.':
            y = random.randint(0, 10)
            if y not in new_array:
                new_array[i] = y
                i+=1
        else:
            i+=1
    print("\n", new_array)


mycode = ''' 
def fullfillTheArray(new_array):
    for _ in new_array:
        print(_, end='')
    i = 0
    while i < (len(new_array)):
        if new_array[i] == '.':
            y = random.randint(0, 10)
            if y not in new_array:
                new_array[i] = y
                i+=1
        else:
            i+=1    
'''

print(timeit.timeit(mycode))