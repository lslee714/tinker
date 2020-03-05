def bubble_sort(aList):
    for i in range(len(aList)):
        swapped = False
        index = 0
        while index < len(aList)-1:
            if aList[index] > aList[index+1]:
                aList[index], aList[index+1] = aList[index+1], aList[index]
                swapped = True
            index += 1
        if not swapped:
            break
    return aList