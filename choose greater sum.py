from itertools import combinations

def choose_greater_sum(maxnum, num_elem, elem):
    listel = list(elem)
    options = list(combinations(listel, num_elem))
    finalones = []
    maior = 0
    for x in range(len(options)):
        soma = sum(options[x])
        if soma >= maior and soma <= maxnum:
            finalones.append([x, sum(options[x])])
            maior = int(soma)
    if maior == 0:
        return "None"
    return int(maior)

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_greater_sum(430, 8, xs))