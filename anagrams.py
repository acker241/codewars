def anagrams(word, words):
    WordDict ={}
    TrueAnams = []
    SetWord = list(set(word))
    for x in range(len(set(word))):
        WordDict[SetWord[x]] = str.count(word,SetWord[x])
    for y in range(len(words)):
        if set(words[y]) == set(word):
            SetWords = list(set(words[y]))
            matches = 0
            for x in range(len(SetWords)):
                if (str.count(words[y],str(SetWords[x]))) == WordDict[(SetWords[x])]:
                    matches +=1
                if matches == len(SetWord):
                    TrueAnams.append(words[y])
    return TrueAnams


AnaList = ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba',
           'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']
print(anagrams('abba', AnaList))