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

def processMovement(input, coordinates, coordinates2, crossingWires):
    X = 0
    Y = 0
    for value in input:
        repeat = int(value[1:])
        if value[:1] == 'R':
            while repeat != 0:
                X += 1
                coordinates.append((X,Y))

                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y))
                    print(f"found: {(X,Y)}")
                    pass
                repeat -= 1
                pass
            pass
        if value[:1] == 'L':
            while repeat != 0:
                X -= 1
                coordinates.append((X,Y))

                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y))
                    print(f"found: {(X,Y)}")
                    pass
                repeat -= 1
                pass
            pass
        if value[:1] == 'U':
            while repeat != 0:
                Y += 1
                coordinates.append((X,Y))

                if (X,Y) in coordinates2:
                    crossingWires.append((X,Y))
                    print(f"found: {(X,Y)}")
                    pass
                repeat -= 1
                pass
            pass
        if value[:1] == 'D':
            while repeat != 0:
                Y -= 1
                coordinates.append((X,Y))

                if (X,Y) in coordinates2 and (X,Y) not in crossingWires:
                    crossingWires.append((X,Y))
                    print(f"found: {(X,Y)}")
                    pass
                repeat -= 1
                pass
            pass
        pass
    pass

processMovement(input1, coordinates1, coordinates2, crossingWires)
processMovement(input2, coordinates2, coordinates1, crossingWires)

print("Done searching.")

print("Search lowest Manhattan distance:")

min = 10000000

for value in crossingWires:
    if min > (abs(value[0]) + abs(value[1])):
        min = (abs(value[0]) + abs(value[1]))
        print(f"Updated minimum: {min}")
        pass
    pass

print(f"\nAnswer: {min}")

#print(f"List1: {coordinates1}\n\n")
#print(f"List2: {coordinates2}")
