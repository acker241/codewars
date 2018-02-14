def int_to_negabinary(i):
    if i == 0 or i == '':
        return 0
    elif i == 1:
        return 1
    else:
        remind = []
        while i != 0:
            i, divresult = divmod(i, -2)
            if divresult < 0:
                i, divresult = i+1, divresult+2
            remind.insert(0,str(divresult))
        return ''.join(remind)

def negabinary_to_int(s):
    if s == 0 or s == '':
        return 0
    elif s == 1:
        return 1
    else:
        negabinary = []
        for x in range(len(s)):
            negabinary.append(int(s[x]))
        varnega = (negabinary[0] * (-2)) + negabinary[1]
        for x in range(2,len(negabinary)):
            varnega = (varnega*(-2))+negabinary[x]
        return varnega