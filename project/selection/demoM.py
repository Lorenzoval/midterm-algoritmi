from project.selection.mSelection import sampleMedianSelect
from project.modules.Testing import *
from math import ceil


def testSMSForM(l, k, stopM, startM=1):
    for i in range(startM, stopM):
        print("sampleMedianSelect with m={} takes {} seconds".format(i, selectionTest(l, k, sampleMedianSelect, i)))


if __name__=="__main__":
    print("List with 250000 elements in ascending order:")
    ordered = generateSortedList(250000)
    testSMSForM(ordered[:], ceil(len(ordered) / 2), 50)
    print("List with 250000 elements in descending order:")
    reverse = generateRevSortedList(249999)
    testSMSForM(reverse[:], ceil(len(reverse) / 2), 50)
    print("List with 250000 random elements:")
    rand = generateRandList(250000)
    testSMSForM(rand[:], ceil(len(rand) / 2), 50)


