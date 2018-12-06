from random import randint


def sample(l, k):
    if type(l) != list and type(l) != tuple:
        raise TypeError("First parameter must be a list or a tuple")
    if type(k) != int:
        raise TypeError("Second parameter must be an integer")

    length = len(l)
    if k > length or k < 0:
        raise ValueError("Second parameter must be a positive integer smaller than len(first parameter)")

    retList = []
    checkList = []

    for i in range(k):  # @UnusedVariable
        j = randint(0, length - 1)
        while j in checkList:
            j = randint(0, length - 1)
        checkList.append(j)
        retList.append(l[j])

    return retList


if __name__ == "__main__":
    testList = [1, 2, 3, 4, 5]
    print("List:", testList)
    newList = sample(testList, 3)
    print("Sample:", newList)
