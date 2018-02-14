def make_negative( number ):
    if number > 0:
        return(number*-1)
    elif number < 0:
        return(number)
    else:
        return(0)


for x in range(-2,5):
    print(make_negative(x))