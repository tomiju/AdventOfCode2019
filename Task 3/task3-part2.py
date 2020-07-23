# Advent Of Code 2019
# Task 3

def resetList():
    f = open("input-task3.txt", "r")
    inputList = []
    for line in f:
        inputList.append(line.replace('\n',',').split(','))

    input1 = inputList[:(len(inputList)//2)][0]
    input2 = inputList[(len(inputList)//2):][0]

    input1 = [i for i in input1 if i] # remove empty strings
    input2 = [i for i in input2 if i] # remove empty strings

    #print(f"test1 {input1}")
    #print(f"test2 {input2}")

    return input1, input2

input1 = []
input2 = []

input1, input2 = resetList() # load input

coordinates1 = []
coordinates2 = []
crossingWires = []
coordinatesWithSteps = []

def processMovement(input, coordinates, coordinates2, crossingWires, coordinatesWithSteps):
    X = 0
    Y = 0
    steps = 0
    for value in input:
        repeat = int(value[1:])
        if value[:1] == 'R':
            while repeat != 0:
                X += 1
                coordinates.append((X,Y))
                steps += 1
                coordinatesWithSteps.append((X,Y,steps))
                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y,steps))
                    print(f"found: {(X,Y,steps)}")
                    pass
                repeat -= 1
                pass
            pass
        if value[:1] == 'L':
            while repeat != 0:
                X -= 1
                coordinates.append((X,Y))
                steps += 1
                coordinatesWithSteps.append((X,Y,steps))
                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y,steps))
                    print(f"found: {(X,Y,steps)}")
                    pass
                repeat -= 1
                pass
            pass
        if value[:1] == 'U':
            while repeat != 0:
                Y += 1
                coordinates.append((X,Y))
                steps += 1
                coordinatesWithSteps.append((X,Y,steps))
                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y,steps))
                    print(f"found: {(X,Y,steps)}")
                    pass
                repeat -= 1
                pass
            pass
        if value[:1] == 'D':
            while repeat != 0:
                Y -= 1
                coordinates.append((X,Y))
                steps += 1
                coordinatesWithSteps.append((X,Y,steps))
                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y,steps))
                    print(f"found: {(X,Y,steps)}")
                    pass
                repeat -= 1
                pass
            pass
        pass
    print("Part done...\n")
    pass

print("Part1:")
processMovement(input1, coordinates1, coordinates2, crossingWires, coordinatesWithSteps)
print("Part2:")
processMovement(input2, coordinates2, coordinates1, crossingWires, coordinatesWithSteps)

print("Done processing.\n")

print("Searching fewest combined steps:")

min = 10000000

for value in coordinatesWithSteps:
    for value2 in crossingWires:
        if (value[0], value[1]) == (value2[0], value2[1]):
            if min > (value[2] + value2[2]):
                min = value[2] + value2[2]
                print(f"Updated minimum: {min}, value1: {value}, value2: {value2}") # 6484 is the correct answer -
                                                                                    # for some reason it continues and finds 2004 (possibly not my bad?)...
                pass
            pass
        pass
    pass

print(f"\nAnswer: {min}")
