import itertools
def permutations(string):
    return list(itertools.permutations(string))
#    letras =[]
#    for x in range(len(string)):
#        letras.append(string[x])
#    level = list(letras)
#    novas = []
#    for x in range(len(letras)-1):
#        for y in range(len(level)):
#            for z in range(len(letras)):
#                if str(level[y]).count(letras[z]) < letras.count(letras[z]):
#                    string = (str(str(level[y])+str(letras[z])))
#                    if novas.count(string) == 0:
#                        novas.append(string)
#        level = list(novas)
#        novas.clear()
#    return level

print(permutations('aabb'))