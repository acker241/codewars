def sum_for_list(lst):
    division = []
    for x in range(len(lst)):
        for y in range(2,lst[x]):
            if divmod(lst[x],y)[1] == 0:
                if y <= 3:
                    division.append(y)
                elif divmod(y,2)[1] != 0:
                    if divmod(y,3) [1] !=0:
                        division.append(y)
    division = list(set(division))
    primesum = []
    for x in range(len(division)):
        primesum.append(0)
    for y in range(len(division)):
        for x in range(len(lst)):
            if divmod(lst[x],division[y])[1] == 0:
                primesum[y] = primesum[y] + lst[x]
    primetup = []
    for x in range(len(division)):
        primetup.append([division[x],primesum[x]])
    return primetup

sum_for_list([12,15])