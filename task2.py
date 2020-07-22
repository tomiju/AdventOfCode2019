# Advent Of Code 2019
# Task 2

def resetList(inputList, input):
    f = open("input-task2.txt", "r")
    inputList = []
    for line in f:
        inputList.append(line.replace('\n','').split(','))

    input = inputList[0]

    #print(inputList[0]) # debug
    return inputList, input

inputList = []
input = []

inputList, input = resetList(inputList, input) # load input

command = 0
number1 = 0
number2 = 0
resultPosition = 0 # position of result

position = 0 # position in code
result = 0
maxLength = len(input)

while input[0] != '19690720':
    for noun in range(100):
        for verb in range(100):

            position1 = 0
            position = 0
            inputList, input = resetList(inputList, input)
            input[position + 1] = noun
            input[position + 2] = verb

            for position1 in range(maxLength):
                position1 = position
                if position + 4 <= maxLength - 1:
                    command = int(input[position])
                    number1 = int(input[position + 1])
                    number2 = int(input[position + 2])
                    resultPosition = int(input[position + 3])
                    #print(f"Deb3: cmd {command}, num1 {number1}, num2 {number2}, resultPosition {resultPosition}")
                    if command == 1:
                        input[resultPosition] = int(input[number1]) + int(input[number2])
                        pass
                    elif command == 2:
                        input[resultPosition] = int(input[number1]) * int(input[number2])
                        pass
                    elif command == 99:
                        break
                    else:
                        print(f"Error cmd: {command}, pos:{position}")
                        exit()
                    position += 4
                else:
                    break

            if int(input[0]) >= 19690720:
                print(f"Answer: noun {noun}, verb {verb}")
                exit()
                pass

            print(f"Value 0: {input[0]}")
            #exit()

#print(input) # debug

for value in input:
    print(value, end =",")
    pass
