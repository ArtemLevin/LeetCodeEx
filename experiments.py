def genFunc(myList):
    for a in myList:
        if a % 2 == 0:
            yield a + 1


print(list(genFunc([0, 1, 2, 3, 4, 5])))
