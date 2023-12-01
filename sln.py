def getContent(fileURL):
    '''
    Getting the content of the URL. To not overwhelm the Advent of code server, I have saved
    the file locally as a text file. There shouldn't be the need for these exceptions as I have included the
    text file in the repo, but it is meant to be good coding practices
    '''
    try:
        with open(fileURL, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{fileUrl}' not found")
        return None
    except Exception as e:
        print(f"Error Occurred: {e}")
        return None

def findCode(textStr):
    '''
    The loops is designed to use two moving pointers of the left and right sides of the string
    When a digit is found, the left index found and right index found bools are tagged true, this will then mark the end of the while loop
    Should the right index become less than the left, that indicates nothing in the string is a digit, so we return 0
    '''
    if(len(textStr) == 0): return 0
    indL = 0
    indLFound = False
    indRFound = False
    indR = len(textStr)-1
    while not(indLFound and indRFound):
        if not indLFound:
            if (textStr[indL]).isdigit():
                indLFound = True
            else:
                indL += 1
        if not indRFound:
            if (textStr[indR]).isdigit():
                indRFound = True
            else:
                indR -= 1
        if indR < indL: return 0
    return int(textStr[indL] + textStr[indR])

def findCode2(textStr):
    '''
    Nearly identical to findCode, this method is modified to first perform a search for substrings within the string
    The goal is to find the lowest index when searching from the left, and the highest when searching from the right
    The right index is then increased by the len of that word - 1 to align with the movements of the right pointer
    The while loop is mostly identical, though it looks to see if either text search values is found before an actual digit
    '''
    if(len(textStr) == 0): return 0
    nameDict = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    minL, maxR = len(textStr), -1
    rightHold = ""
    lVal, rVal = -1, -1
    for val,out in nameDict.items():
        leftV = textStr.find(val)
        rightV = textStr.rfind(val)
        if leftV != -1:
            if leftV < minL: 
                minL = leftV
                lVal = out
        if rightV != -1:
            if rightV > maxR: 
                maxR = rightV
                rightHold = val
                rVal = out
    maxR += len(rightHold)-1
    indL = 0
    indLFound = False
    indRFound = False
    indR = len(textStr)-1
    while not(indLFound and indRFound):
        if not indLFound:
            if (textStr[indL]).isdigit() or indL == minL:
                indLFound = True
            else:
                indL += 1
        if not indRFound:
            if (textStr[indR]).isdigit() or indR == maxR:
                indRFound = True
            else:
                indR -= 1
        if indR < indL: return 0
    if indL == minL:
        retL = lVal
    else:
        retL = textStr[indL]
    if indR == maxR:
        retR = rVal
    else:
        retR = textStr[indR]
    return int(retL + retR)


if __name__ == "__main__":
    textStr = getContent("input.txt")
    textSplit = textStr.splitlines()
    #maxSum = sum([findCode(x) for x in textSplit])
    #print(maxSum)
    maxSum2 = sum([findCode2(x) for x in textSplit])
    print(maxSum2)