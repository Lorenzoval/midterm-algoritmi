from project.__init__ import printSwitch
from datastruct.Stack import PilaArrayList as Stack
from selection.Selection import partitionDet, quickSelectDet, quickSelectRand


# QuickSort - RECURSIVE

def quickSort(l, selectionAlgorithm, *otherParameters):
    recursiveQuickSort(l, 0, len(l) - 1, selectionAlgorithm, *otherParameters)


def recursiveQuickSort(l, left, right, selectionAlgorithm, *otherParameters):
    if printSwitch.dumpOperations:
        print("recursiveQuickSort({},{},{})".format(left, right, selectionAlgorithm.__name__))

    if left >= right:
        return

    k = int(len(l[left:right+1]) / 2.0) + 1  # index of the median
    median = selectionAlgorithm(l[left:right + 1], k, *otherParameters)  # pass a copy of the list to selectionAlgorithm

    if printSwitch.dumpOperations:
        print("Selected median:", median)

    mid = partitionDet(l, left, right, median)

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))

    recursiveQuickSort(l, left, mid - 1, selectionAlgorithm, *otherParameters)
    recursiveQuickSort(l, mid + 1, right, selectionAlgorithm, *otherParameters)

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))


# End of QuickSort - RECURSIVE

# QuickSort - ITERATIVE

def quickSortIter(l, selectionAlgorithm, *otherParameters):
    iterativeQuickSort(l, 0, len(l) - 1, selectionAlgorithm, *otherParameters)


def iterativeQuickSort(l, left, right, selectionAlgorithm, *otherParameters):
    theStack = Stack()
    theStack.push(left)
    theStack.push(right)
    while not theStack.isEmpty():
        right = theStack.pop()
        left = theStack.pop()

        if printSwitch.dumpOperations:
            print("quickSortIter-step({},{},{})".format(left, right, selectionAlgorithm.__name__))

        if right <= left:
            continue

        k = int(len(l[left:right + 1]) / 2.0) + 1
        median = selectionAlgorithm(l[left:right + 1], k, *otherParameters)

        mid = partitionDet(l, left, right, median)

        theStack.push(left)
        theStack.push(mid - 1)

        theStack.push(mid + 1)
        theStack.push(right)


# End of QuickSort - ITERATIVE


if __name__ == "__main__":
    l = [4, 1234, 34, 566, 8, 2, 5346, 8, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]
    print(l)

    quickSort(l, quickSelectRand)
    # quickSortIter(l, quickSelectRand)
    # quickSort(l, quickSelectDet, 3)
    # quickSortIter(l, quickSelectDet, 3)

    # output should be: 2,2,3,3,4,7,7,8,8,8,34,42,43,57,87,263,566,845,1234,5346]
    print(l)
