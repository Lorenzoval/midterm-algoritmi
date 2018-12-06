from time import time
import random
from project.modules.Sample import sample


def sampleTest(inputList, k, sampleFunc):
    l = inputList[:]
    random.seed(1)  # both functions will use the same seed during test
    start = time()
    sampleFunc(l, k)
    return time() - start


def generateRandList(steps, maxValue=None):
    if maxValue == None:
        maxValue = steps
    retList = []
    for i in range(steps):  # @UnusedVariable
        retList.append(random.randint(0, maxValue))

    return retList


if __name__ == "__main__":
    small = 100
    medium = 1000
    big = 10000

    print("Sample of len(list)/2 elements:")
    smallList = generateRandList(small)
    print("Small list ({} elements):".format(small))
    runningTime = sampleTest(smallList, int(small/2), sample)
    print("'sample' required {} seconds".format(runningTime))
    runningTime = sampleTest(smallList, int(small/2), random.sample)
    print("'random.sample' required {} seconds".format(runningTime))

    medList = generateRandList(medium)
    print("Medium list ({} elements):".format(medium))
    runningTime = sampleTest(medList, int(medium/2), sample)
    print("'sample' required {} seconds".format(runningTime))
    runningTime = sampleTest(medList, int(medium/2), random.sample)
    print("'random.sample' required {} seconds".format(runningTime))

    bigList = generateRandList(big)
    print("Big list ({} elements):".format(big))
    runningTime = sampleTest(bigList, int(big/2), sample)
    print("'sample' required {} seconds".format(runningTime))
    runningTime = sampleTest(bigList, int(big/2), random.sample)
    print("'random.sample' required {} seconds".format(runningTime))

