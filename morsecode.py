def DecodeMorse(MorseCode):
    dict = {'.-': 'A','-...': 'B','-.-.': 'C','-..': 'D','.': 'E','..-.': "F",'--.': 'G','....': 'H' }
    dict['..'] = 'I'
    dict['.---'] = 'J'
    dict['-.-'] = 'K'
    dict['.-..'] = 'L'
    dict['--'] = 'M'
    dict['-.'] = 'N'
    dict['---'] = 'O'
    dict['.--.'] = 'P'
    dict['--.-'] = 'Q'
    dict['.-.'] = 'R'
    dict['...'] = 'S'
    dict['-'] = 'T'
    dict['..-'] = 'U'
    dict['...-'] = 'V'
    dict['.--'] = 'W'
    dict['-..-'] = 'X'
    dict['-.--'] = 'Y'
    dict['--..'] = 'Z'
    dict['-----'] = '0'
    dict['.----'] = '1'
    dict['..---'] = '2'
    dict['...--'] = '3'
    dict['....-'] = '4'
    dict['.....'] = '5'
    dict['-....'] = '6'
    dict['--...'] = '7'
    dict['---..'] = '8'
    dict['----.'] = '9'

    #pegar palavras
    wordsindex = MorseCode.find('   ')
    morseword = []
    if wordsindex > 0:
        morseword.append(MorseCode[0:wordsindex])
        while len(morseword) < MorseCode.count('   ')+1:
            if len(morseword) == MorseCode.count('   '):
                morseword.append(MorseCode[wordsindex+3:len(MorseCode)])
            else:
                previndex = int(wordsindex)
                wordsindex = MorseCode.find('   ',wordsindex+1)
                morseword.append(MorseCode[previndex+3:wordsindex])

    #decode words
    frase = ''
    for x in range(len(morseword)):
        WordDecode = str(morseword[x])
        frase = frase+(dict[WordDecode[0:WordDecode.index(' ')]])
        spaceindex = WordDecode.index(' ')
        y = 0
        while y < WordDecode.count(' '):
            if y == WordDecode.count(' ')-1:
                frase = frase+(dict[WordDecode[spaceindex+1:len(WordDecode)]])
            else:
                prevspaceindex = int(spaceindex)
                spaceindex = WordDecode.index(' ',prevspaceindex+1)
                frase = frase+(dict[WordDecode[prevspaceindex+1:spaceindex]])
            y += 1
        frase = frase+' '
    return frase
print(DecodeMorse('.... . -.--   .--- ..- -.. .'))
#should return "HEY JUDE"

