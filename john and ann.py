def john(n):
    johnkata = [0]
    annkata = [1]
    for x in range(1,n):
        johnkata.append(x-(annkata[johnkata[x-1]]))
        annkata.append(x - (johnkata[annkata[x - 1]]))
    return johnkata

def ann(n):
    johnkata = [0]
    annkata = [1]
    for x in range(1,n):
        johnkata.append(x-(annkata[johnkata[x-1]]))
        annkata.append(x - (johnkata[annkata[x - 1]]))
    return annkata

def sum_john(n):
    return sum(john(n))
def sum_ann(n):
    return sum(ann(n))