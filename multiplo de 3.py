def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        result = number * (number-1)
        number -= 2
        while number > 0:
            result = result * number
            number -= 1
        return result

def find_mult_3(num):
    NumList = list(set(str(num)))
    NumDic = {}
    for x in range(len(NumList)):
        NumDic[NumList[x]] = str(num).count(NumList[x])
    NumCluster = [str(num)]
    MultCluster = []
    y, a = False, 0
    contagem1dig = 0
    if divmod(num,3)[1] == 0:
        MultCluster.append(str(num))
    while y == False:
        for x in range(len(NumCluster[a])):
            stringpt1 = NumCluster[a][0:x]
            stringpt2 = NumCluster[a][x + 1:len(NumCluster[a])]
            NewNumString = stringpt1 + stringpt2
            if NumCluster.count(NewNumString) == 0 and NewNumString != '':
                NumCluster.append(NewNumString)
                if divmod(int(NewNumString),3)[1] == 0 and NewNumString != '0':
                    MultCluster.append(NewNumString)
                if len(NewNumString) == 1:
                    contagem1dig += 1
        a += 1
        if contagem1dig == len(NumList):
            y = True
    combinations = 0
    for x in range(len(MultCluster)):
        NumList = list(set(MultCluster[x]))
        NumDic = {}
        for a in range(len(NumList)):
            NumDic[NumList[a]] = str(MultCluster[x]).count(NumList[a])
        firstfactorial = factorial(len(MultCluster[x]))
        sndfactorial = factorial(list(NumDic.values())[0])
        for y in range(1,len(NumDic)):
            sndfactorial = sndfactorial * factorial(list(NumDic.values())[y])
        numcombs = firstfactorial/sndfactorial
        combinations = combinations + numcombs
        print(str(MultCluster[x])+' tem '+str(numcombs))
    HighestList = []
    for x in range(len(MultCluster[0])):
        HighestList.append((MultCluster[0][x]))
    HighestList.sort()
    HighestList.reverse()
    HighNum = int(''.join(HighestList))
    return [int(combinations), HighNum]

print(find_mult_3(6063))
