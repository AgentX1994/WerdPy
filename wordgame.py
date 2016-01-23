# Programmed John Asper (AgentX1994) 2016
# Werd Nerd originally by Porter Venn

import random

def loadDict(wordlist, filename):
    f = open(filename, 'r')
    for word in f:
        wordlist.append(word.rstrip())
    f.close()

def get_letters(letters):
    for i in range(12):
        letters.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

a = []
loadDict(a,"dictionary.txt")
print(a)

if "add" in a:
    print("\"add\" is in the dictionary.")
else:
    print("ERROR: \"add\" is NOT in the dictionary.")

letters = []
get_letters(letters)

print(letters)
