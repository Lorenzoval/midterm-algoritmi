import random
from time import time


def generateRandList(steps, maxValue=None):
    if maxValue is None:
        maxValue = steps
    retList = []
    for _ in range(steps):  # @UnusedVariable
        retList.append(random.randint(0, maxValue))

    return retList


def generateSortedList(stop, start=0, step=1):
    return list(range(start, stop, step))


def generateRevSortedList(start, stop=-1, step=-1):
    return list(range(start, stop, step))


def selectionTest(l, k, selectionAlgorithm, *otherParameters):
    start = time()
    selectionAlgorithm(l, k, *otherParameters)
    return time() - start


if __name__=="__main__":
    l = generateRandList(10, 5)
    print(l)
    m = generateSortedList(10)
    print(m)
    n = generateRevSortedList(10)
    print(n)
