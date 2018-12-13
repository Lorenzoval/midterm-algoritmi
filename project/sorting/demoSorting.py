import sorting.Sorting as Sorting
import project.sorting.mSorting as mSorting
from project.selection.mSelection import sampleMedianSelect
from selection.Selection import quickSelectDet, quickSelectRand
from project.modules.Testing import *
from time import time


def printResults(l, sortingAlgorithm, *otherParameters):
    if not otherParameters:
        print("{} required {} seconds".format(sortingAlgorithm.__name__, sortingTest(l, sortingAlgorithm)))
    else:
        if callable(otherParameters[0]):  # if otherParameters[0] is a function
            print("{}({}) required {} seconds".format(sortingAlgorithm.__name__, otherParameters[0].__name__,
                                              sortingTest(l, sortingAlgorithm, *otherParameters)))
        else:
            print("{} required {} seconds".format(sortingAlgorithm.__name__, sortingTest(l, sortingAlgorithm,
                                                                                         *otherParameters)))


def increasingLenAvgTest(sortingAlgorithm, genListFunc, num, maxLen, steps, *otherParameters):
    # per semplicita' si assuma maxLen % steps = 0
    delta = int(maxLen / steps)
    testDict = {}
    for i in range(1, steps + 1):
        testDict[i * delta] = 0
    for _ in range(num):
        temp = delta
        while temp <= maxLen:
            testList = genListFunc(temp)
            testDict[temp] += sortingTest(testList, sortingAlgorithm, *otherParameters)
            temp += delta
    for k in testDict:
        testDict[k] = testDict[k] / num
    return testDict


def builtInTest(l):
    start = time()
    l.sort()
    return time() - start


def printBuiltIn(l):
    print("Built-in sorting method required {} seconds".format(builtInTest(l)))


def increasingLenAvgBuiltIn(genListFunc, num, maxLen, steps):
    delta = int(maxLen / steps)
    testDict = {}
    for i in range(1, steps + 1):
        testDict[i * delta] = 0
    for _ in range(num):
        temp = delta
        while temp <= maxLen:
            testList = genListFunc(temp)
            testDict[temp] += builtInTest(testList)
            temp += delta
    for k in testDict:
        testDict[k] = testDict[k] / num
    return testDict


if __name__=="__main__":
    amountSlow = 5000
    amount = 100000

    print("List with {} elements in ascending order:".format(amount))
    ordered = generateSortedList(amount)
    printResults(ordered[:], Sorting.quickSort)
    printResults(ordered[:], mSorting.quickSort, quickSelectRand)
    printResults(ordered[:], mSorting.quickSort, quickSelectDet, 10)
    printResults(ordered[:], mSorting.quickSort, sampleMedianSelect, 4)
    printBuiltIn(ordered[:])
    print("List with {} elements in descending order:".format(amount))
    reverse = generateRevSortedList(amount)
    printResults(ordered[:], Sorting.quickSort)
    printResults(reverse[:], mSorting.quickSort, quickSelectRand)
    printResults(reverse[:], mSorting.quickSort, quickSelectDet, 10)
    printResults(reverse[:], mSorting.quickSort, sampleMedianSelect, 4)
    printBuiltIn(reverse[:])
    print("List with {} random elements:".format(amount))
    rand = generateRandList(amount)
    printResults(ordered[:], Sorting.quickSort)
    printResults(rand[:], mSorting.quickSort, quickSelectRand)
    printResults(rand[:], mSorting.quickSort, quickSelectDet, 10)
    printResults(rand[:], mSorting.quickSort, sampleMedianSelect, 4)
    printBuiltIn(rand[:])

    # print("{} elements in random order".format(amountSlow))
    # print("SelectionSort:")
    # print(increasingLenAvgTest(Sorting.selectionSort, generateRandList, 20, amountSlow, 10))
    # print("InsertionSortDown:")
    # print(increasingLenAvgTest(Sorting.insertionSortDown, generateRandList, 20, amountSlow, 10))
    # print("InsertionSortUp:")
    # print(increasingLenAvgTest(Sorting.insertionSortUp, generateRandList, 20, amountSlow, 10))
    # print("BubbleSort:")
    # print(increasingLenAvgTest(Sorting.bubbleSort, generateRandList, 20, amountSlow, 10))
    # print("Heap Sort:")
    # print(increasingLenAvgTest(Sorting.heapSort, generateRandList, 20, amountSlow, 10))
    # print("QuickSort non deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateRandList, 20, amountSlow, 10))
    # print("QuickSort deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort,generateRandList, 20, amountSlow, 10, True))
    # print("MergeSort:")
    # print(increasingLenAvgTest(Sorting.mergeSort, generateRandList, 20, amountSlow, 10))
    # print("RadixSort:")
    # print(increasingLenAvgTest(Sorting.radixSort, generateRandList, 20, amountSlow, 10, amountSlow, 100))
    # print("QuickSort_QuickSelectRand:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRandList, 20, amountSlow, 10, quickSelectRand))
    # print("QuickSort_QuickSelectDet:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRandList, 20, amountSlow, 10, quickSelectDet, 10))
    # print("QuickSort_SampleMedianSelect:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRandList, 20, amountSlow, 10, sampleMedianSelect, 4))
    # print("Built-in:")
    # print(increasingLenAvgBuiltIn(generateRandList, 20, amountSlow, 10))
    #
    # print("{} elements in ascending order".format(amountSlow))
    # print("SelectionSort:")
    # print(increasingLenAvgTest(Sorting.selectionSort, generateSortedList, 20, amountSlow, 10))
    # print("InsertionSortDown:")
    # print(increasingLenAvgTest(Sorting.insertionSortDown, generateSortedList, 20, amountSlow, 10))
    # print("InsertionSortUp:")
    # print(increasingLenAvgTest(Sorting.insertionSortUp, generateSortedList, 20, amountSlow, 10))
    # print("BubbleSort:")
    # print(increasingLenAvgTest(Sorting.bubbleSort, generateSortedList, 20, amountSlow, 10))
    # print("Heap Sort:")
    # print(increasingLenAvgTest(Sorting.heapSort, generateSortedList, 20, amountSlow, 10))
    # print("QuickSort non deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateSortedList, 20, amountSlow, 10))
    # print("QuickSort deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateSortedList, 20, amountSlow, 10, True))
    # print("MergeSort:")
    # print(increasingLenAvgTest(Sorting.mergeSort, generateSortedList, 20, amountSlow, 10))
    # print("RadixSort:")
    # print(increasingLenAvgTest(Sorting.radixSort, generateSortedList, 20, amountSlow, 10, amountSlow, 100))
    # print("QuickSort_QuickSelectRand:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateSortedList, 20, amountSlow, 10, quickSelectRand))
    # print("QuickSort_QuickSelectDet:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateSortedList, 20, amountSlow, 10, quickSelectDet, 10))
    # print("QuickSort_SampleMedianSelect:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateSortedList, 20, amountSlow, 10, sampleMedianSelect, 4))
    # print("Built-in:")
    # print(increasingLenAvgBuiltIn(generateSortedList, 20, amountSlow, 10))
    #
    # print("{} elements in descending order".format(amountSlow))
    # print("SelectionSort:")
    # print(increasingLenAvgTest(Sorting.selectionSort, generateRevSortedList, 20, amountSlow, 10))
    # print("InsertionSortDown:")
    # print(increasingLenAvgTest(Sorting.insertionSortDown, generateRevSortedList, 20, amountSlow, 10))
    # print("InsertionSortUp:")
    # print(increasingLenAvgTest(Sorting.insertionSortUp, generateRevSortedList, 20, amountSlow, 10))
    # print("BubbleSort:")
    # print(increasingLenAvgTest(Sorting.bubbleSort, generateRevSortedList, 20, amountSlow, 10))
    # print("Heap Sort:")
    # print(increasingLenAvgTest(Sorting.heapSort, generateRevSortedList, 20, amountSlow, 10))
    # print("QuickSort non deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateRevSortedList, 20, amountSlow, 10))
    # print("QuickSort deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateRevSortedList, 20, amountSlow, 10, True))
    # print("MergeSort:")
    # print(increasingLenAvgTest(Sorting.mergeSort, generateRevSortedList, 20, amountSlow, 10))
    # print("RadixSort:")
    # print(increasingLenAvgTest(Sorting.radixSort, generateRevSortedList, 20, amountSlow, 10, amountSlow, 100))
    # print("QuickSort_QuickSelectRand:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRevSortedList, 20, amountSlow, 10, quickSelectRand))
    # print("QuickSort_QuickSelectDet:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRevSortedList, 20, amountSlow, 10, quickSelectDet, 10))
    # print("QuickSort_SampleMedianSelect:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRevSortedList, 20, amountSlow, 10, sampleMedianSelect, 4))
    # print("Built-in:")
    # print(increasingLenAvgBuiltIn(generateRevSortedList, 20, amountSlow, 10))
    #
    # print("{} elements in random order, only non-quadratic algorithms".format(amount))
    # print("Heap Sort:")
    # print(increasingLenAvgTest(Sorting.heapSort, generateRandList, 20, amount, 10))
    # print("QuickSort non deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateRandList, 20, amount, 10))
    # print("QuickSort deterministico:")
    # print(increasingLenAvgTest(Sorting.quickSort, generateRandList, 20, amount, 10, True))
    # print("MergeSort:")
    # print(increasingLenAvgTest(Sorting.mergeSort, generateRandList, 20, amount, 10))
    # print("RadixSort:")
    # print(increasingLenAvgTest(Sorting.radixSort, generateRandList, 20, amount, 10, amount, 400))
    # print("QuickSort_QuickSelectRand:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRandList, 20, amount, 10, quickSelectRand))
    # print("QuickSort_QuickSelectDet:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRandList, 20, amount, 10, quickSelectDet, 10))
    # print("QuickSort_SampleMedianSelect:")
    # print(increasingLenAvgTest(mSorting.quickSort, generateRandList, 20, amount, 10, sampleMedianSelect, 4))
    # print("Built-in:")
    # print(increasingLenAvgBuiltIn(generateRandList, 20, amount, 10))
