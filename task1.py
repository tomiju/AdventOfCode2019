# Advent Of Code 2019
# Task 1

import math

f = open("input-task1.txt", "r")

inputList = []

for line in f:
    inputList.append(line.replace('\n',''))



#print(inputList)

result = 0

for number in inputList:
    partialNumber = math.floor((int(number)/3)) - 2
    while partialNumber > 0:
        result += partialNumber
        partialNumber = math.floor((int(partialNumber)/3)) - 2



print(result)
