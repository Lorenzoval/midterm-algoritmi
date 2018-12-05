from project.__init__ import printSwitch
from datastruct.Stack import PilaArrayList as Stack
import random


# QuickSort - RECURSIVE, deterministic and non-deterministic

def quickSort(l, det=False):
    recursiveQuickSort(l, 0, len(l) - 1, det)


def recursiveQuickSort(l, left, right, det=False):
    if printSwitch.dumpOperations:
        print("recursiveQuickSort({},{})".format(left, right))

    if left >= right:
        return

    mid = partition(l, left, right, det)
    recursiveQuickSort(l, left, mid - 1, det)
    recursiveQuickSort(l, mid + 1, right, det)

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))


def partition(l, left, right, det=False):
    inf = left
    sup = right + 1

    if not det:
        random.seed(1)
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left]  # exchange first elem with the randomically chosen one

    mid = left # the median is the first elem of the array

    if printSwitch.dumpOperations:
        print("Selected median:", l[mid])

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))

    return sup


# End of QuickSort - RECURSIVE, deterministic and non-deterministic

# QuickSort - ITERATIVE, deterministic and non-deterministic

def quickSortIter(l, det=False):
    iterativeQuickSort(l, 0, len(l) - 1, det)


def iterativeQuickSort(l, left, right, det=False):
    theStack = Stack()
    theStack.push(left)
    theStack.push(right)
    while not theStack.isEmpty():
        right = theStack.pop()
        left = theStack.pop()

        if printSwitch.dumpOperations:
            print("quickSortIter-step({},{})".format(left, right))

        if right <= left:
            continue

        mid = partition(l, left, right, det)

        theStack.push(left)
        theStack.push(mid - 1)

        theStack.push(mid + 1)
        theStack.push(right)


# End of QuickSort - ITERATIVE, deterministic and non-deterministic


if __name__ == "__main__":
    l = [4, 1234, 34, 566, 8, 2, 5346, 8, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]
    print(l)

    quickSort(l)
    # quickSortIter(l)

    # output should be: 2,2,3,3,4,7,7,8,8,8,34,42,43,57,87,263,566,845,1234,5346]
    print(l)
