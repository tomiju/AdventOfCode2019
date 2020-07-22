# Advent Of Code 2019
# Task 4 (part 2)

# input range: 264793-803935

start = 264793
end = 803935

count = 0

def checkRules(number):
    pom = str(number)

    # length
    if len(pom) != 6:
        print(f"Debug len: {len(pom)}")
        return False
        pass

    # within range
    if number < 264793 or number > 803935:
        print(f"Debug range: {number}")
        return False
        pass

    prev = 0
    bool = False
    bool_found = False # if 2 adjacent numbers are definitely found - don't care about the rest
    largerGroup = False

    # 2 adjacent digits are the same + digits never decrease
    for char in pom:
        if prev != 0:

            # decreasing numbers
            if int(char) < int(prev):
                #print(f"Debug decreasing: {number}")
                return False
                pass

            # adjacent numbers
            if bool == True and char == prev:
                bool = False
                largerGroup = True
                #print(f"Debug adjacent digits: {number}, bool: {bool}, largerGroup: {largerGroup}, chars: {char} + {prev}")
                pass
            elif bool == False and char != prev:
                largerGroup = False
                pass
            elif bool == True and char != prev:
                bool_found = True;

            if bool != True or largerGroup == True:
                if largerGroup != True:
                    if char == prev:
                        bool = True
                        largerGroup = False
                        #print(f"Debug adjacent digits: {number}, bool: {bool}, largerGroup: {largerGroup}, chars: {char} + {prev}\n")
                        pass
                    pass
            pass

        prev = char
        pass

    # if you end up with two adjacent numbers, then the password is correct - bool_found = true
    if bool == True:
        bool_found = True
        pass

    if bool_found:
        #print(f"Found: {number}")
        return True
        pass
    else:
        #print(f"Fail: {number}")
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
