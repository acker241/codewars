def find_mult_3(num):

    ListStrNum = []
    ListDivided = []

    a, b = len(str(num)), len(str(num))
    a, b = (a - 1), (b * (a - 1))

    for x in range(len(str(num))):
        ListStrNum.append(str(num)[x])
    AllStrings = []
    for x in range(len(ListStrNum)):
        AllStrings.append(ListStrNum[x])
        PrevDiv = int(ListStrNum[x]) / 3
        if int(PrevDiv) == PrevDiv and int(ListStrNum[x]) != 0:
            if ListDivided.count(int(ListStrNum[x])) == 0:
                ListDivided.append(int(ListStrNum[x]))

    DicStrings = {}
    for x in range(len(set(ListStrNum))):
        ListaSetDic = list(set(ListStrNum))
        VarSet = ListaSetDic[x]
        DicStrings[VarSet] = ListStrNum.count(VarSet)

    for x in range(len(ListStrNum)):
        y = 0
        while y != b:
            for z in range(len(AllStrings)):
                NumberStrings = []
                if len(AllStrings[z]) > x:
                    NumString = AllStrings[z]
                    for loopstrings in range(len(NumString)):
                        NumberStrings.append(NumString[loopstrings])
                    for s in range(len(ListStrNum)):
                        if NumberStrings.count(ListStrNum[s]) < DicStrings[ListStrNum[s]]:
                            NewNum = AllStrings[z]+(ListStrNum[s])
                            if AllStrings.count(NewNum) == 0:
                                AllStrings.append(NewNum)
                                Div = int(NewNum)/3
                                if int(Div) == Div and ListDivided.count(int(NewNum)) == 0:
                                    ListDivided.append(int(NewNum))
                                    print('Num '+str(len(ListDivided))+' adicionado!')
            y +=1
        a, b = (a - 1), (b * (a - 1))
    print(ListDivided)
    ListDivided.sort()
    return [len(ListDivided),ListDivided[len(ListDivided)-1]]

print(find_mult_3(426530))