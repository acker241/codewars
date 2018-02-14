def palindrome_chain_length(n):
    def reverse(number):
        newnumber = ''
        for x in range(len(str(number))):
            newnumber = newnumber+str(number)[(x-(len(str(number))-1))*-1]
        return int(newnumber)
    if n == reverse(n):
        return 0
    IsPalindrom = False
    tries = 1
    n = n + reverse(n)
    while IsPalindrom == False:
        if n == reverse(n):
            return tries
        else:
            n = n+reverse(n)
            tries += 1

print(palindrome_chain_length(87))