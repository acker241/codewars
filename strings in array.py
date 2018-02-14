def in_array(array1, array2):
    FinalArray = []
    for x in range(len(array1)):
        y = 0
        while y != len(array2):
            if str.count(array2[y],array1[x]) != 0:
                if FinalArray.count(array1[x]) == 0:
                    FinalArray.append(array1[x])
                    y = len(array2)
                else:
                    y +=1
            else:
                y += 1
    return (sorted(FinalArray))

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

print(in_array(a1,a2))