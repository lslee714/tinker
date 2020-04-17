import math

def repeated_strings(string, totalLength, character='a'):
    numberOfAsInString = string.count(character)
    leftOver = totalLength % len(string)
    wholeStringRepeats = (totalLength - leftOver) / len(string)
    return int(wholeStringRepeats * numberOfAsInString + (string[:leftOver].count(character)))