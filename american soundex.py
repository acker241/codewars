def soundex(name):
    print(name)
    letters = [['b','1'],['f','1'],['p','1'],['v','1'],['c', '2'], ['g', '2'], ['j', '2'], ['k', '2'], ['q', '2'],
    ['s', '2'], ['x', '2'], ['z', '2'],['d', '3'], ['t', '3'],['l', '4'], ['m', '5'],['n', '5'], ['r', '6']]
    names = []
    if str(name).count(' ') == 0:
        names.append(str(name).lower())
    else:
        names.append(str(str(name)[0:str(name).index(' ')]).lower())
        names.append(str(str(name)[str(name).index(' ')+1:len(str(name))]).lower())
    for x in range(len(names)):
        lista = []
        for y in range(1,len(names[x])):
            if lista.count(names[x][y]) == 0:
                lista.append(names[x][y])
        print(lista)
        finalsoundex = str.capitalize(names[x][0])
        for y in range(1,len(lista)):
            for z in range(len(letters)):
                if lista[y] == letters[z][0] and len(finalsoundex) < 4:
                    finalsoundex = finalsoundex+letters[z][1]
        if len(finalsoundex) < 4:
            finalsoundex = finalsoundex+('0'*(4-len(finalsoundex)))
        names.pop(x)
        names.insert(x,finalsoundex)
    return ' '.join(names)
print(soundex('zxqurlwbx'))