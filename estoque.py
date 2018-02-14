import openpyxl
import csv
from string import ascii_uppercase as ASCII
relatorio = "C:\\Estoque MCA\\Relatorio.csv"

opencsv = open(relatorio)
listabruta = list(csv.reader(opencsv))
referencias = []
linhas = {} #número das linhas referentes a cada referencia
listadic = {} #linhas tratadas
colunas = {} #dicionario para transformar numero em coluna

#vai ser o main loop, mas por enquanto pega a referência e descrição
for x in range(len(listabruta)):
    frase = str(listabruta[x])
    if frase[2:14].count('.') == 2 and frase[2:14].count('-') == 1:
        descricao = frase[15:frase.index('Faixa')]
        descricao =''.join(descricao.split(';'))
        ref = frase[2:13]
        linhas[ref] = x
        for z in range((len(descricao)-4),len(descricao)):
            if descricao[z].isdigit():
                descricao = descricao[0:z]
                referencias.append([ref,descricao])
                break
    elif frase.count('Grade') > 0:
        temp = []
        splitlist = frase[2:len(frase) - 2].split(';')
        for z in range(len(splitlist)):
            if splitlist[z] == '03/jun':
                temp.append('03/06')
            elif splitlist[z] == '06/set':
                temp.append('06/09')
            elif splitlist[z] == '09/dez':
                temp.append('09/12')
            elif splitlist[z] == 'dez/18':
                temp.append('12/18')
            elif splitlist[z] != '':
                temp.append(splitlist[z])
        listadic[x] = list(temp)
        temp.clear()
    else:
        splitlist = frase[2:len(frase)-2].split(';')
        if splitlist[1].isdigit():
            digit = int(splitlist[1])
            splitlist.pop(1)
            splitlist.insert(1,digit)
        elif splitlist[1] == '':
            splitlist[1] = ''
        else:
            string = ''
            digit = ''
            for z in range(len(splitlist[1])):
                if splitlist[1][z].isdigit():
                    digit = digit+splitlist[1][z]
                else:
                    string = string+splitlist[1][z]
            splitlist[0] = splitlist[0]+string
            if digit.isdigit():
                splitlist[1] = int(digit)
            else:
                splitlist[1] = ''
        for z in range(1,len(splitlist)):
            if type(splitlist[z]) is str and splitlist[z].isdigit():
                splitlist[z] = int(splitlist[z])
        listadic[x] = list(splitlist)

#range de linhas da listabruta que corresponde a cada referência
for x in range(len(referencias)):
    if x >= len(referencias)-1:
        linhas[referencias[x][0]] = [linhas[referencias[x][0]]+1, len(listabruta)]
    else:
        linhas[referencias[x][0]] = [linhas[referencias[x][0]]+1,linhas[referencias[x+1][0]]]

for x in range(len(ASCII)):
    colunas[x] = ASCII[x]

planilha = openpyxl.Workbook()
ativa = planilha.active
linhaatual = 0
for x in range(len(referencias)):
    linhaatual += 1
    ativa['A'+str(linhaatual)] = referencias[x][0]
    ativa['B'+str(linhaatual)] = referencias[x][1]
    for z in range(linhas[referencias[x][0]][0],linhas[referencias[x][0]][1]):
        linhaatual +=1
        inserir = listadic[z]
        for y in range(len(inserir)):
            ativa[colunas[y]+str(linhaatual)] = inserir[y]

planilha.save("C:\\Estoque MCA\\Relatorio_tratado.xlsx")