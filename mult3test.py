import datetime
import itertools
def find_mult_3(num):

    ListNum = []
    for x in range(len(str(num))):
        ListNum.append(str(num)[x])
    ListLvl = []
    ListDivided = []
    for x in range(1,len(ListNum)+1):
        Time = datetime.datetime.now()
        ListLvl=list(itertools.permutations(ListNum,x))
        for y in range(len(ListLvl)):
            NumToDivide = int(''.join(ListLvl[y]))
            if NumToDivide/3 == int(NumToDivide/3) and ListDivided.count(NumToDivide) == 0:
                ListDivided.append(NumToDivide)
        print("List Length: "+str(len(ListLvl))+". Cycle: "+str(x)+'.')
        print("Time Taken: "+str(datetime.datetime.now()-Time))
        ListLvl = []
    ListDivided.sort(reverse=True)
    print(ListDivided)
    return[len(ListDivided),ListDivided[0]]

ListToTest = [362,6063,7766553322]

for x in range(len(ListToTest)):
    print(find_mult_3(ListToTest[x]))