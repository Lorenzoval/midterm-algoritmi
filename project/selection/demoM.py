from project.selection.mSelection import sampleMedianSelect
from project.modules.Testing import *
from math import ceil


def testSMSForM(l, k, stopM, startM=1):
    for i in range(startM, stopM):
        print("sampleMedianSelect with m={} takes {} seconds".format(i, selectionTest(l, k, sampleMedianSelect, i)))


def minKeyDict(d):
    val = list(d.values())
    m = min(val)
    for k in d:
        if d[k] == m:
            return k


def avgBestCaseM(l, k, num, stopM, startM=1):
    """
    Popola un dizionario myDict con (chiave = m, valore = tempo medio di esecuzione su num tests).
    Restituisce la chiave con valore minimo.
    """
    myDict = {}
    keys = range(startM, stopM)
    for k in keys:
        myDict[k] = 0
    for _ in range(num):
        for i in range(startM, stopM):
            myDict[i] += selectionTest(l[:], k, sampleMedianSelect, i)
    for j in keys:
        myDict[j] = myDict[j] / num
    # print(myDict)
    return minKeyDict(myDict)  # oppure return min(myDict, key=myDict.get)


if __name__=="__main__":
    print("List with 25000 elements in ascending order:")
    ordered = generateSortedList(25000)
    testSMSForM(ordered[:], ceil(len(ordered) / 2), 50)
    print("Launching 20 tests, on average, the best case was achieved with m =",
           avgBestCaseM(ordered[:], ceil(len(ordered) / 2), 20, 50, 3))
    print("List with 25000 elements in descending order:")
    reverse = generateRevSortedList(24999)
    testSMSForM(reverse[:], ceil(len(reverse) / 2), 50)
    print("Launching 20 tests, on average, the best case was achieved with m =",
           avgBestCaseM(reverse[:], ceil(len(reverse) / 2), 20, 50, 3))
    print("List with 25000 random elements:")
    rand = generateRandList(25000)
    testSMSForM(rand[:], ceil(len(rand) / 2), 50)
    print("Launching 20 tests, on average, the best case was achieved with m =",
           avgBestCaseM(rand[:], ceil(len(rand) / 2), 20, 50, 3))
