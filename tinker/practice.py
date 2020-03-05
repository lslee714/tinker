def get_pairs(ar):
    itemByItems = {}
    for i in ar:
        itemByItems.setdefault(i, []).append(i)
    pairs = 0
    for item, items in itemByItems.items():
        if len(items) >= 2:
            numberOfPairs = int(len(items) / 2)
            pairs += numberOfPairs
    return pairs


def get_valleys(string):
    elevation = 0
    numValleys = 0
    for substring in string:
        lowered = substring.lower()
        if lowered == 'u':
            elevation += 1
        elif lowered == 'd':
            elevation -= 1
        if elevation == 0 and lowered == 'u':
            numValleys += 1
    return numValleys

def is_safe(number):
    return number ==0


def get_min_jumps(arr):
    jumps = 0
    currentPosition = 0
    while currentPosition != len(arr) - 1:
        nextPosition = currentPosition + 1
        nextNextPosition = currentPosition + 2
        try:
            hasTwoMore = arr[nextNextPosition] is not None
        except IndexError:
            hasTwoMore = False

        if hasTwoMore and arr[nextNextPosition] == 0:
            currentPosition = nextNextPosition
        else:
            currentPosition = nextPosition
        jumps += 1
    return jumps

import operator

def mostFrequent(arr):
    valsAndCounts={}
    for val in arr:
        valsAndCounts.setdefault(val, 1)
        valsAndCounts[val] += 1
    keys = list(valsAndCounts.keys())
    vals = list(valsAndCounts.values())

    maxVal = max(vals)
    maxValIndex = vals.index(maxVal)
    return keys[maxValIndex]

def equalizeArray(arr):
    mostFrequentVal = mostFrequent(arr)
    deletions = 0
    for val in arr:
        if val != mostFrequentVal:
            deletions += 1
    return deletions


def get_moves_bottom_left(board, itemsBeforeQueen):
    moves = 0
    rowWithQueen = [row for row in board if 'QUNN' in row][0]
    rowIndex = board.index(rowWithQueen)

    for n in range(itemsBeforeQueen):
        correspondingRow = board[rowIndex+n]
        diagonalItem = correspondingRow[n]
        if diagonalItem == 'XXXX':
            return moves
        moves += 1
    return moves

def get_moves_bottom_right(board, queenPosition):
    moves = 0
    rowWithQueen = [row for row in board if 'QUNN' in row][0]
    rowIndex = board.index(rowWithQueen)

    awayFromQueen = 1
    for n in range(rowIndex+1, len(board)):
        print(n)
        correspondingRow = board[n]
        print(correspondingRow)
        try:
            diagonalItem = correspondingRow[queenPosition+awayFromQueen]
            awayFromQueen += 1
        except IndexError:
            return moves
        if diagonalItem == 'XXXX':
            return moves
        moves += 1
    return moves


def get_moves_down(board, queenPosition):
    moves = 0
    print(queenPosition)
    rowWithQueen = [row for row in board if 'QUNN' in row][0]
    rowIndex = board.index(rowWithQueen)
    for n in range(rowIndex+1, len(board)):
        correspondingRow = board[n]
        verticalItem = correspondingRow[queenPosition]
        if verticalItem == 'XXXX':
            return moves
        moves += 1
    return moves


def get_moves_up(board, queenPosition):
    moves = 0
    rowWithQueen = [row for row in board if 'QUNN' in row][0]
    rowIndex = board.index(rowWithQueen)
    for n in range(rowIndex):
        correspondingRow = board[n]
        verticalItem = correspondingRow[queenPosition]
        if verticalItem == 'XXXX':
            return moves
        moves += 1
    return moves

def get_moves_top_right(board, queenPosition):
    moves = 0
    rowWithQueen = [row for row in board if 'QUNN' in row][0]
    rowIndex = board.index(rowWithQueen)
    for n in range(rowIndex):
        correspondingRow = board[n]
        diagonalItem = correspondingRow[queenPosition+n]
        if diagonalItem == 'XXXX':
            return moves
        moves += 1
    return moves

def get_moves_top_left(board, queenPosition):
    moves = 0

    if queenPosition == 0 or queenPosition == len(board)-1:
        return moves
    for n in range(queenPosition):
        correspondingRow = board[n]
        diagonalItem = correspondingRow[n]
        if diagonalItem == 'XXXX':
            return moves
        moves += 1
    return moves

def get_moves_right(rowWithQueen, boardLength, queenPos):
    moves = 0
    for n in range(queenPos+1, boardLength):
        horizontalItem = rowWithQueen[n]
        if horizontalItem == 'XXXX':
            return moves
        moves += 1
    return moves

def get_moves_left(rowWithQueen, queenPos):
    moves = 0
    for n in range(queenPos-1, -1 ,-1):
        horizontalItem = rowWithQueen[n]
        if horizontalItem == 'XXXX':
            return moves
        moves += 1
    return moves

def queensAttack(rowsAndCols, numObstacles, queenRowPos, queenColPos, obstacleDems):

    row = ['None' for n in range(rowsAndCols)]
    board = [row.copy() for n in range(rowsAndCols)]
    for oRow, oCol in obstacleDems:
        board[-oRow][oCol-1] = 'XXXX'

    board[-queenRowPos][queenColPos-1] = 'QUNN'
    rowWithQueen = board[-queenRowPos]
    queenPosition = rowWithQueen.index('QUNN')
    itemsBeforeQueen = len(rowWithQueen[:queenPosition])
    moves = 0

    print("BOARD", board)
    movesToBottomLeft = get_moves_bottom_left(board, itemsBeforeQueen)
    print("MOVES BOTTOM LEFT", movesToBottomLeft)
    if movesToBottomLeft:
        moves += movesToBottomLeft
    #traverse down
    movesDown = get_moves_down(board, queenPosition)
    print("MOVES DOWN", movesDown)
    if movesDown:
        moves += movesDown

    #traverse down to the right
    movesToBottomRight = get_moves_bottom_right(board, queenPosition)
    print("MOVES BOTTOM RIGHT", movesToBottomRight)
    if movesToBottomRight:
        moves += movesToBottomRight
    #traverse up
    movesUp = get_moves_up(board, queenPosition)
    print("MOVES UP", movesUp)
    if movesUp:
        moves += movesUp

    #traverse to the top right
    movesTopRight = get_moves_top_right(board, queenPosition)
    print("MOVES TOP RIGHT", movesTopRight)
    if movesTopRight:
        moves += movesTopRight

    #Traverse to the top left
    movesTopLeft = get_moves_top_left(board, queenPosition)
    print("MOVES TOP LEFT", movesTopLeft)
    if movesTopLeft:
        moves += movesTopLeft

    movesToRight = get_moves_right(rowWithQueen, len(board), queenPosition)
    print("MOVES RIGHT", movesToRight)
    if movesToRight:
        moves += movesToRight


    movesToLeft = get_moves_left(rowWithQueen, queenPosition)
    print("MOVES LEFT", movesToLeft)
    if movesToLeft:
        moves += movesToLeft

    for row in board:
        print(row)
    return moves

def minimumBribes(aList):
    if any(index < value-3 for index, value in enumerate(aList)):
        return 'Too chaotic'
    else:
        bribes = 0
        for n in range(len(aList)):
            swapped = False
            index = 0
            while index < len(aList)-1:
                checking = aList[index]
                on = aList[index+1]
                if checking > on:
                    aList[index], aList[index+1] = aList[index+1], aList[index]
                    swapped = True
                    bribes += 1
                index += 1
            if not swapped:
                break
        return bribes

def min_swaps(aList):
    swap = 0
    i = 0
    while i < len(aList):
        if aList[i] == i+1:
            i += 1
            continue
        else:
            whereItShouldBe = aList[i] - 1
            #put value where it should be
            aList[whereItShouldBe], aList[i] = aList[i], aList[whereItShouldBe]
            swap +=1
    return swap


from collections import Counter
def find_makeable_words(words, charset):
    makeableWords = []
    for word in words:
        canMake = True
        charactersByCount = Counter(word)
        for char, count in charactersByCount.items():
            if char not in charset or charset.count(char) < count:
                canMake = False
        if canMake:
            makeableWords.append(word)
    return makeableWords


def find_anagram_count(string):
    anagram_dict = {}
    count = 0
    #sliding window
    for i in range(1, len(string)):
        for j in range(len(string)-i+1):
            substr = string[j:j+i]
            sortedSubstr = sorted(substr)
            if sortedSubstr:
                anagramKey = str(sortedSubstr)
                if anagramKey in anagram_dict:
                    count += anagram_dict[anagramKey]
                    anagram_dict[anagramKey] += 1
                else:
                    anagram_dict[anagramKey] = 1
    return count

from collections import defaultdict, Counter

def count_triplets(aList, commonFactor):

    # secondTripleCounts = defaultdict(int)
    # thirdTripleCounts = defaultdict(int)
    # count = 0
    # for value in aList:
    #     count += thirdTripleCounts[value]
    #     print(f"VAL {value} TOTAL {count}")
    #
    #     secondTripleCounts[value * commonFactor] += 1
    #     thirdTripleCounts[value * commonFactor] += secondTripleCounts[value]
    # return count
    doublets = {}
    triplets = {}
    count = 0
    for val in aList:
        # if val in triplets indicates the triplet already completed,
        # the count need be incremented
        if val in triplets:
            count += triplets[val]

        # if val in doublets, it is the second number of the triplet,
        # your successor (third element val*r) need be added or incremented in the triplets dict
        # because is a potential triplet
        if val in doublets:
            if val * commonFactor in triplets:
                triplets[val * commonFactor] += doublets[val]
            else:
                triplets[val * commonFactor] = doublets[val]

        # else, val is the first element of the triplet, so,
        # your successor (second element val*commonFactor) need be added or incremented in the doublets dict
        # because is a potential triplet
        if val * commonFactor in doublets:
            doublets[val * commonFactor] += 1
        else:
            doublets[val * commonFactor] = 1

    return count

def insert(struct, val, frequencies, counts):
    struct.append(val)
    counts[frequencies[val]] -= 1
    frequencies[val] += len(struct)
    counts[frequencies[val]] += 1
    return None

def delete(struct, val, frequencies, counts):
    if val in struct:
        counts[frequencies[val]] -= 1
        struct.remove(val)
        frequencies[val] = len(struct)
        counts[frequencies[val]] += 1
    return None

def check_frequency(struct, frequencyVal, frequencies, counts):
    return 1 if frequencyVal in counts and counts[frequencyVal] > 0 else 0

def frequency_query(queries):
    results = []
    frequencies = defaultdict(int)
    counts = defaultdict(int)
    for query in queries:
        operationKey = query[0]
        value = query[1]
        if operationKey == 1:
            counts[frequencies[value]] -= 1
            frequencies[value] +=1
            counts[frequencies[value]] += 1
        elif operationKey == 2:
            if frequencies[value] >0:
                counts[frequencies[value]] -= 1
                frequencies[value] -=1
                counts[frequencies[value]] += 1

        elif operationKey == 3: #could be else but handle specifically for 3
            if value in counts and counts[value] > 0:
                results.append(1)
            else:
                results.append(0)
    return results

# from statistics import median, StatisticsError
#
# def activity_notifications(aListOfDays, minimumDaysForTrigger):
#     if len(aListOfDays) <= minimumDaysForTrigger:
#         return 0
#     notifications = 0
#     alreadyCheckedDays = {}
#     while True:
#         daysToCheck = aListOfDays[0:minimumDaysForTrigger+1]
#         if len(daysToCheck) < minimumDaysForTrigger + 1:
#             break
#
#         dayToCompare = daysToCheck.pop()
#         if tuple(daysToCheck) in alreadyCheckedDays:
#             medianSpent = daysToCheck[tuple(daysToCheck)]
#         else:
#             medianSpent = median(sorted(daysToCheck))
#         if dayToCompare >= medianSpent*2:
#             notifications+=1
#         aListOfDays.pop(0)
#     return notifications


from collections import deque


class RollingMedian:
    def __init__(self, maxlen):
        self.histogram = [0] * 201
        self.window = deque([], maxlen)
        self.maxlen = maxlen

    def append(self, x):
        if len(self.window) == self.maxlen:
            y = self.window.popleft()
            self.histogram[y] -= 1
        self.window.append(x)
        self.histogram[x] += 1

    def median(self):
        a = self.maxlen // 2
        b = a + 1
        running_sum = 0
        med_a = None
        med_b = None
        for idx, val in enumerate(self.histogram):
            running_sum += val
            if running_sum >= a and med_a is None:
                med_a = idx
            if running_sum >= b:
                med_b = idx
                break

        if self.maxlen % 2 == 0:
            # even case
            return (med_a + med_b) / 2
        else:
            # odd case
            return med_b


def activity_notifications(expenditure, d):
    notifications = 0
    roll = RollingMedian(d)
    for x in expenditure:
        print(x)
        if len(roll.window) == d:
            median = roll.median()
            if x >= 2 * median:
                notifications += 1
        roll.append(x)

    return notifications