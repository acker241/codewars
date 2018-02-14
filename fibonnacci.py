def findFib(fibn):
    fiblist = [0, 1]
    if fibn == 0 or fibn == 1:
        return(fiblist[fibn])
    else:
        for x in range(2,(fibn+1)):
            fiblist.append(fiblist[x-1]+fiblist[x-2])
        return (fiblist[fibn])

def productFib(prod):
    x = 0
    while x < prod:
        fib1 = findFib(x)
        fib2 = findFib(x+1)
        prevprod = fib1*fib2
        if prevprod < prod:
            x += 1
        elif prevprod == prod:
            return([fib1,fib2,True])
        else: return([fib1,fib2,False])

print(productFib(800))

print(findFib(10))