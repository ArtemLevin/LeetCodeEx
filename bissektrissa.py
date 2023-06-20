import random
list = [i for i in range(10)]
myList = [t for t in [random.randrange(100) for t in range(10)] if any(t<5)]
print(myList)