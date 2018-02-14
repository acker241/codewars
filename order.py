def order(sentence):
    WordList = []
    SentenceList = str(sentence).split()
    for x in range(1,10):
        for y in range(len(SentenceList)):
            if str(SentenceList[y]).find(str(x)) != -1:
                WordList.insert(x,SentenceList[y])
    return(str.join(" ",WordList))