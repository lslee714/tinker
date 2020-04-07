def get_first_or_third_list_sum(beginIdx, aList):
    return sum(aList[beginIdx: beginIdx+3])


def get_hourglass_sum_at_idx(idx, firstList, oneAheadList, twoAheadList):
    firstListSum = get_first_or_third_list_sum(idx, firstList)
    thirdListSum = get_first_or_third_list_sum(idx, twoAheadList)
    oneAheadListSum = oneAheadList[idx+1]
    return firstListSum + thirdListSum + oneAheadListSum



def hourglass(twoDimensionalList):
    maxHourGlassableNumberIndex = len(twoDimensionalList[0]) - 2
    maxHourGlassableListIndex = len(twoDimensionalList) - 2
    hourGlassSums = []
    for listIdx, subList in enumerate(twoDimensionalList[:maxHourGlassableListIndex]):
        for numberIdx, number in enumerate(subList[:maxHourGlassableNumberIndex]):
            hourGlassSumAtIdx = get_hourglass_sum_at_idx(numberIdx, subList, twoDimensionalList[listIdx+1], twoDimensionalList[listIdx+2])
            hourGlassSums.append(hourGlassSumAtIdx)
    return max(hourGlassSums)