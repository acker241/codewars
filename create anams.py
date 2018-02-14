def permutations(string):
    if len(string) == 1:
        return [string]
    ListStr = []
    for x in range(len(string)):
        ListStr.append(string[x])
    ListWork = list(ListStr)
    ListFinal = []
    NextList = []
    for x in range(len(ListStr)):
        for y in range(len(ListWork)):
            for z in range(len(ListStr)):
                if str(ListWork[y]).count(ListStr[z]) < ListStr.count(ListStr[z]):
                    newstr = ListWork[y]+ListStr[z]
                    if NextList.count(newstr) == 0:
                        NextList.append(newstr)
                        if len(newstr) == len(string):
                            ListFinal.append(newstr)
        ListWork = list(NextList)
        NextList.clear()
        print('='*20)
        print(len(ListWork))
        print(x)
    print('x'*20)
    print(len(ListFinal))
    return ListFinal



permutations('aaaabcdeffffqw')