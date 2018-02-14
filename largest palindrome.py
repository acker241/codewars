def numeric_palindrome(*args):
    def check_palindrome(numbertocheck):
        numbertocheck = str(numbertocheck)
        numberset = sorted(list(set(str(numbertocheck))),reverse=True)
        evenodddic, oddcount = {},0
        for x in range(len(numberset)):
            evenorodd = numbertocheck.count(numberset[x])
            if divmod(evenorodd,2)[1] > 0:
                oddcount +=1
                if oddcount > 1:
                    return False
                else:
                    evenodddic[numberset[x]] = evenorodd
            else:
                evenodddic[numberset[x]] = evenorodd
        largpalind = ''
        splitpalind = ''
        if oddcount > 0:
            for x in range(len(numberset)):
                largpalind = largpalind+(str(numberset[x])*divmod(evenodddic[numberset[x]],2)[0])
                if divmod(evenodddic[numberset[x]], 2)[1] > 0:
                    splitpalind = str(numberset[x])
            largpalind = largpalind+splitpalind+largpalind[::-1]
            return largpalind
        else:
            for x in range(len(numberset)):
                largpalind = largpalind+(str(numberset[x])*divmod(evenodddic[numberset[x]],2)[0])
            largpalind = largpalind+largpalind[::-1]
            return largpalind

    numbers = sorted(list(args))
    all_comb = []
    mult_results = []
    for x in range(len(numbers)):
        all_comb.append([numbers[x]])
        mult_results.append(numbers[x])
    #create all combs
    for x in range(len(numbers)):
        for y in range(len(all_comb)):
            if len(all_comb[y]) == x:
                for z in range(len(numbers)):
                    current_comb = list(all_comb[y])
                    if current_comb.count(numbers[z]) < numbers.count(numbers[z]):
                        current_comb.append(numbers[z])
                    current_comb = sorted(current_comb)
                    if all_comb.count(current_comb) == 0:
                        all_comb.append(current_comb)
    for x in range(len(all_comb)):
        if len(all_comb[x]) > 1:
            for z in range(len(all_comb[x])):
                if z == 0:
                    multiplied = all_comb[x][z]
                else:
                    multiplied = multiplied * all_comb[x][z]
            mult_results.append(multiplied)
    mult_results = list(sorted(mult_results,reverse=True))
    for x in range(len(mult_results)):
        checagem = check_palindrome(mult_results[x])
        if checagem != False:
            return checagem

print(numeric_palindrome(70,82,47,42))
