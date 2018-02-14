
def Mult6(NumToMult):
    def Mult2(NumToMult2):
        return NumToMult2*2
    def Mult3(NumToMult3):
        return NumToMult3*3
    return Mult2(Mult3(NumToMult))

teststring = 'Francisco'
stringc = 4
print(teststring[0:stringc])
print(teststring[stringc:len(teststring)])