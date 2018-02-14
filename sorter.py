import random, datetime

tamanho = 3000
divisor = 100
Origem = []
Shuffle = []
for x in range(1,tamanho+1):
    Origem.append(x)

criacao_shuffle = datetime.datetime.now()
correct = 0
while correct == 0:
    num_to_add = random.choice(Origem)
    Origem.pop(Origem.index(num_to_add))
    Shuffle.append(num_to_add)
    if len(Shuffle) == tamanho:
        correct = 1
print('Embaralhado demorou',datetime.datetime.now()-criacao_shuffle,sep=' ')


def testing_sort(list):
    right = 0
    while right == 0:
        for pos in range(len(list)):
            if pos+1<len(list)-1 and list[pos] > list[pos+1]:
                num_menor = list[pos+1]
                list.pop(pos+1)
                list.insert(pos,num_menor)
                pos = pos + 2
            elif pos == len(list)-1:
                if list[pos] < list[pos-1]:
                    num_menor = list[pos]
                    list.pop(pos)
                    list.insert(pos-1,num_menor)

        for check in range(len(list)):
            if check+1<len(list)-1 and list[check] > list[check+1]:
                break
            elif check == len(list)-1:
                right = 1
    return list


def check_if_sorted(list):
    for check in range(len(list)):
        if check+1<len(list)-1 and list[check] > list[check+1]:
            return False
        elif check == len(list)-1:
            return True


def interval_sorting(list):
    final = []
    num_of_divs = int(len(list)/divisor)
    for x in range(num_of_divs):
        max_range = ((x+1)*divisor)
        min_range = ((x+1)*divisor)-divisor
        partial = []
        for y in range(min_range,max_range):
            partial.append(list[y])
        partly_sorted = testing_sort(partial)
        for y in range(len(partly_sorted)):
            final.append(partly_sorted[y])
    return final

Init = datetime.datetime.now()


div_list = [5,10,100,1000]
for x in range(len(div_list)):
    divisor = div_list[x]
    init = datetime.datetime.now()
    if tamanho > divisor:
        list_to_sort = list(Shuffle)
        while check_if_sorted(list_to_sort) == False:
            list_to_sort = list(testing_sort(interval_sorting(list_to_sort)))
    else:
        Shuffle = testing_sort(Shuffle)
    print('Divisor', div_list[x],'demorou',datetime.datetime.now()-init,sep=' ')
