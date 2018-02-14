def prefill(n,v):
    list = []
    if n == 0:
        return []
    try:
        for x in range(int(n)):
            list.append(v)
        return list
    except ValueError:
        return (str(n) + " is invalid")
    except TypeError:
        return (str(n)+" is invalid")
