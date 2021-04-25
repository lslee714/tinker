def bubble_sort(aList):
    for idx, element in enumerate(aList):
        swapped = False
        start = idx + 1
        while start < len(aList):
            next_element = aList[start]
            if element > next_element:
                aList[idx], aList[start] = aList[start], aList[idx]
                swapped = True
            start += 1
        if not swapped:
            break
    return aList