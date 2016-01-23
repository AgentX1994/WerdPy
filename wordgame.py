def loadDict(wordlist, filename):
    f = open(filename, 'r')
    for word in f:
        wordlist.append(word.rstrip())
    f.close()

a = []
loadDict(a,"dictionary.txt")
print(a)
