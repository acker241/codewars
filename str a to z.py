test1 = ["aretheyhere", "yestheyarehere"]
test2 = ["loopingisfunbutdangerous", "lessdangerousthancoding"]
test3 = ["inmanylanguages", "theresapairoffunctions"]

def longest(s1,s2):

    maior = s1 + s2

    print(maior)

    unicaMaior = set(maior)
    lista = list(unicaMaior)
    lista.sort()
    TamanhoFinal = len(lista)

    tamanholista = len(lista)


    OutputFinal = str(lista[0])

    for x in range(1,TamanhoFinal):
        OutputFinal = OutputFinal + lista[x]

    return(OutputFinal)

#teste1 = longest(test1[0],test1[1])
teste2 = longest(test2[0],test2[1])
#teste3 = longest(test3[0],test3[1])

#print(teste1)
print(teste2)
#print(teste3)