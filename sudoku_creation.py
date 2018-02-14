import random
from itertools import permutations
from datetime import datetime

numbers = [1,2,3,4,5,6,7,8,9]

perms = list(permutations(numbers))

def criar_sudoku():
    def compara_linhaad1(linhabase, linhanova):
        count = 0
        for y in range(3):
            if linhabase[0:3].count(linhanova[y]) != 0:
                count += 1
        for y in range(3, 6):
            if linhabase[3:6].count(linhanova[y]) != 0:
                count += 1
        for y in range(6, 9):
            if linhabase[6:9].count(linhanova[y]) != 0:
                count += 1
        if count == 0:
            return linhanova
        else:
            return None
    def compara_linhaad2(linhabase, linhabase1, linhanova):
        count = 0
        for y in range(3):
            if linhabase[0:3].count(linhanova[y]) != 0 or linhabase1[0:3].count(linhanova[y]) != 0:
                count += 1
        for y in range(3, 6):
            if linhabase[3:6].count(linhanova[y]) != 0 or linhabase1[3:6].count(linhanova[y]) != 0:
                count += 1
        for y in range(6, 9):
            if linhabase[6:9].count(linhanova[y]) != 0 or linhabase1[6:9].count(linhanova[y]) != 0:
                count += 1
        if count == 0:
            return linhanova
        else:
            return None
    def comparar_linhas_existentes(linhanova):
        linhas_existentes = []
        linhanova = list(linhanova)
        if linha0 != 0:
            linhas_existentes.append(linha0)
        if linha1 != 0:
            linhas_existentes.append(linha1)
        if linha2 != 0:
            linhas_existentes.append(linha2)
        if linha3 != 0:
            linhas_existentes.append(linha3)
        if linha4 != 0:
            linhas_existentes.append(linha4)
        if linha5 != 0:
            linhas_existentes.append(linha5)
        if linha6 != 0:
            linhas_existentes.append(linha6)
        if linha7 != 0:
            linhas_existentes.append(linha7)
        if linha8 != 0:
            linhas_existentes.append(linha8)
        for x in range(len(linhas_existentes)):
            for y in range(9):
                if linhanova[y] == linhas_existentes[x][y]:
                    return None
        return linhanova

    linha1, linha2, linha4, linha5, linha7, linha8 = 0, 0, 0, 0, 0, 0
    linha0 = list(random.choice(perms))
    linha3 = list(random.choice(perms))
    linha6 = list(random.choice(perms))

    condition = False
    while condition == False:
        matches = 0
        for x in range(9):
            if linha3[x] == linha0[x]:
                matches += 1
                break
        if matches == 0:
            condition = True
        else:
            linha3 = list(random.choice(perms))

    condition = False
    while condition == False:
        matches = 0
        for x in range(9):
            if linha6[x] == linha0[x] or linha6[x] == linha3[x]:
                matches +=1
                break
        if matches == 0:
            condition = True
        else:
            linha6 = list(random.choice(perms))

    matches = 0
    #linha1
    for x in range(len(perms)):
        if compara_linhaad1(linha0,perms[x]) != None:
            linhanova = comparar_linhas_existentes(perms[x])
            if linhanova != None:
                linha1 = linhanova
    if linha1 == 0:
        linha1 = [0,0,0,0,0,0,0,0,0]

    #linha 2
    for x in range(len(perms)):
        if compara_linhaad2(linha0,linha1,perms[x]) != None:
            linhanova = comparar_linhas_existentes(perms[x])
            if linhanova != None:
                linha2 = linhanova
    if linha2 == 0:
        linha2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #linha4
    for x in range(len(perms)):
        if compara_linhaad1(linha3, perms[x]) != None:
            linhanova = comparar_linhas_existentes(perms[x])
            if linhanova != None:
                linha4 = linhanova
    if linha4 == 0:
        linha4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #linha 5
    for x in range(len(perms)):
        if compara_linhaad2(linha3,linha4,perms[x]) != None:
            linhanova = comparar_linhas_existentes(perms[x])
            if linhanova != None:
                linha5 = linhanova
    if linha5 == 0:
        linha5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #linha7
    for x in range(len(perms)):
        if compara_linhaad1(linha6, perms[x]) != None:
            linhanova = comparar_linhas_existentes(perms[x])
            if linhanova != None:
                linha6 = linhanova
    if linha7 == 0:
        linha7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #linha 8
    for x in range(len(perms)):
        if compara_linhaad2(linha6,linha7,perms[x]) != None:
            linhanova = comparar_linhas_existentes(perms[x])
            if linhanova != None:
                linha8 = linhanova
    if linha8 == 0:
        linha8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    todas_linhas = [linha0,linha1,linha2,linha3,linha4,linha5,linha6,linha7,linha8]
    return todas_linhas

correto = 0
tentativas = 0

while correto == 0:
    currenttime = datetime.now()
    todas_linhas = criar_sudoku()
    erros = 0
    for x in range(len(todas_linhas)):
        if erros != 0:
            break
        if todas_linhas[x] == [0,0,0,0,0,0,0,0,0]:
            erros +=1
            break
    if erros == 0:
        correto +=1
        print(todas_linhas)
    else:
        tentativas +=1
        #if divmod(tentativas,10)[1] == 0:
        print("Tentativa "+str(tentativas)+" - Tempo: "+str(datetime.now() - currenttime))

