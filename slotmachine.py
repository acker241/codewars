def fruit(reels, spins):
    slottypes = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
    slotDict = {}
    for x in range(10):
        slotDict[slottypes[x]] = (x-10)*-1
    SlotRolls = []
    for x in range(len(spins)):
        SlotRolls.append(reels[x][spins[x]])
    SlotUniques = list(set(SlotRolls))
    contagem = len(SlotUniques)
    SlotResults = {}
    if contagem == 3:
        return 0
    elif contagem ==1:
        return slotDict[SlotUniques[0]]*10
    elif contagem ==2:
        for x in range(contagem):
            SlotResults[SlotRolls.count(SlotUniques[x])] = SlotUniques[x]
        if SlotResults[1] == 'Wild':
            return slotDict[SlotResults[2]]*2
        else:
            return slotDict[SlotResults[2]]

reel = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [0,0,0]

print(fruit([reel,reel,reel],spin))

reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
reel3 = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
spin = [5,4,3]
print(fruit([reel1,reel2,reel3],spin))
#0

reel1 = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
reel3 = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
spin = [0,0,1]
#("Should return: '3'")
print(fruit([reel1,reel2,reel3],spin))