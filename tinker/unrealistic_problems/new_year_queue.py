

def new_year_queue(aList):
    """Returns the number of movements an array had to make to get to aList"""
    if any(item for index, item in enumerate(aList) if item - (index+1) > 2):
        return "Too chaotic"

    moves = 0
    for _ in aList:
        swapped = False
        index = 0
        while index < len(aList)-1:
            if aList[index] > aList[index+1]:
                moves += 1
                aList[index], aList[index+1] = aList[index+1], aList[index]
                swapped = True
            index += 1
        if not swapped:
            break
    return moves




        
        
