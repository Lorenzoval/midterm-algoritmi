from project.selection.mSelection import sampleMedianSelect
from selection.Selection import quickSelectDet, quickSelectRand
from project.modules.Testing import *
from math import ceil


def printResults(l, k, selectionAlgorithm, *otherParameters):
    print("{} required {} seconds".format(selectionAlgorithm.__name__, selectionTest(l, k, selectionAlgorithm,
                                                                                     *otherParameters)))


def increasingLenAvgTest(selectionAlgorithm, genListFunc, num, maxLen, steps, *otherParameters):
    # per semplicita' si assuma maxLen % steps = 0
    delta = int(maxLen / steps)
    testDict = {}
    for i in range(1, steps + 1):
        testDict[i * delta] = 0
    for _ in range(num):
        temp = delta
        while temp <= maxLen:
            testList = genListFunc(int(temp))
            k = ceil(len(testList) / 2)
            testDict[temp] += selectionTest(testList, k, selectionAlgorithm, *otherParameters)
            temp += delta
    for k in testDict:
        testDict[k] = testDict[k] / num
    return testDict


if __name__=="__main__":
    amount = 250000
    print("List with {} elements in ascending order:".format(amount))
    ordered = generateSortedList(amount)
    printResults(ordered[:], ceil(len(ordered) / 2), quickSelectRand)
    printResults(ordered[:], ceil(len(ordered) / 2), quickSelectDet, 10)
    printResults(ordered[:], ceil(len(ordered) / 2), sampleMedianSelect, 4)
    print("List with {} elements in descending order:".format(amount))
    reverse = generateRevSortedList(amount)
    printResults(reverse[:], ceil(len(reverse) / 2), quickSelectRand)
    printResults(reverse[:], ceil(len(reverse) / 2), quickSelectDet, 10)
    printResults(reverse[:], ceil(len(reverse) / 2), sampleMedianSelect, 4)
    print("List with {} random elements:".format(amount))
    rand = generateRandList(amount)
    printResults(rand[:], ceil(len(rand) / 2), quickSelectRand)
    printResults(rand[:], ceil(len(rand) / 2), quickSelectDet, 10)
    printResults(rand[:], ceil(len(rand) / 2), sampleMedianSelect, 4)
    # print(increasingLenAvgTest(quickSelectRand, generateRandList, 20, amount, 10))
    # print(increasingLenAvgTest(quickSelectDet, generateRandList, 20, amount, 10, 10))
    # print(increasingLenAvgTest(sampleMedianSelect, generateRandList, 20, amount, 10, 4))
    # print(increasingLenAvgTest(quickSelectRand, generateSortedList, 20, amount, 10))
    # print(increasingLenAvgTest(quickSelectDet, generateSortedList, 20, amount, 10, 10))
    # print(increasingLenAvgTest(sampleMedianSelect, generateSortedList, 20, amount, 10, 4))
    # print(increasingLenAvgTest(quickSelectRand, generateRevSortedList, 20, amount, 10))
    # print(increasingLenAvgTest(quickSelectDet, generateRevSortedList, 20, amount, 10, 10))
    # print(increasingLenAvgTest(sampleMedianSelect, generateRevSortedList, 20, amount, 10, 4))
