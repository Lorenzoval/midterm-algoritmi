from project.selection.__init__ import printSwitch
from selection.Selection import partitionDet, trivialSelect
from random import sample
from math import ceil


# BEGIN
""" 
    SAMPLE MEDIAN SELECT
    Sceglie un sottoinsieme V della lista in input contenente m elementi scelti in modo random.
    Ne calcola il mediano ed utilizza quest'ultimo come perno per la partition.
"""


def sampleMedianSelect(l, k, m):
    if k <= 0 or k > len(l):
        return None
    return recursiveSampleMedianSelect(l, 0, len(l) - 1, k, m)


def recursiveSampleMedianSelect(l, left, right, k, m):
    if printSwitch.dumpOperations:
        print("recursiveSampleMedianSelect({},{},{},{})".format(left, right, k, m))

    if left > right:
        return

    if left == right and k - 1 == left:
        return l[k - 1]

    if len(l[left:right + 1]) <= m:  # se si ricorre su una lista di dimesione <= m, utilizzare un altro algoritmo
        if printSwitch.dumpOperations:
            print("Length <=", m)
        med = trivialSelect(l[left: right + 1], k - left)
        if printSwitch.dumpOperations:
            print("return:", med)
        return med

    V = sample(l[left:right + 1], m)
    if printSwitch.dumpOperations:
        print("V:", V)
    pivot = trivialSelect(V, ceil(m / 2))
    if printSwitch.dumpOperations:
        print("Selected median:", pivot)

    mid = partitionDet(l, left, right, pivot)
    if printSwitch.dumpOperations:
        print("mid: {}".format(mid))

    if k - 1 == mid:
        return l[mid]
    if k - 1 < mid:
        return recursiveSampleMedianSelect(l, left, mid - 1, k, m)
    else:
        return recursiveSampleMedianSelect(l, mid + 1, right, k, m)


# END


if __name__ == '__main__':
    basel = [5, 34, 26, 1, 4, 2, 17, 50, 41]
    k = 5
    l = list(basel)
    print(l)
    print(sampleMedianSelect(l, k, 3))
    print(l)
