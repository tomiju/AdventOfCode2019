# Advent Of Code 2019
# Task 4 (part 1)

# input range: 264793-803935

start = 264793
end = 803935

count = 0

def checkRules(number):
    pom = str(number)

    # length
    if len(pom) != 6:
        #print(f"Debug len: {len(pom)}")
        return False
        pass

    # within range
    if number < 264793 or number > 803935:
        #print(f"Debug range: {number}")
        return False
        pass

    prev = 0
    bool = False

    # 2 adjacent digits are the same + digits never decrease
    for char in pom:
        if prev != 0:
            if int(char) < int(prev):
                #print(f"Debug decreasing: {number}")
                return False
                pass

            if bool != True:
                if char == prev:
                    #print(f"Debug adjacent digits: {number}")
                    bool = True
                    pass
                pass
            pass
        prev = char
        pass

    if bool:
        #print(f"Found: {number}")
        return True
        pass
    else:
        return False

    pass

def generatePasswords(count):
    for value in range(264793,803936):
        if checkRules(value) == True:
            count += 1
        pass
    pass
    print(f"Answer: {count}")


# main
print("Counting all possible passwords:")
generatePasswords(count)
