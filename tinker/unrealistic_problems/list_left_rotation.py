def list_left_rotation(aList, numberOfRots):
    newList = aList[:]
    for rot in range(numberOfRots):
        newList.append(newList.pop(0))
    return newList
    
    