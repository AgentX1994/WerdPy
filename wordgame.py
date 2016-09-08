# Programmed John Asper (AgentX1994) 2016
# Werd Nerd originally by Porter Venn

import random
from threading import Timer, Thread
import sys
from tkinter import *

class WordGame(Thread):

    def __init__(self, d):
        Thread.__init__(self)
        self.dict = d                    # Allowed words
        self.letters = get_letters()     # The 12 selected letters
        print(self.letters)
        self.cur_letters = get_letters() # A copy for the current word
        self.word = []                   # The word that is currently being spelled
        self.words = []                  # Words that have been spelled
        self.running = False             # Whether the game is currently running
        self.scored = False              # Whether the current game has been scored
        self.score = 0                   # The score of this game

    def keyReleased(self, event):
        c = event.char
        if c.upper() in self.cur_letters:
            print(c.upper())
            self.word.append(c.upper())
            self.cur_letters.remove(c.upper())
        elif event.keysym == 'Return':
            print("Enter")
            self.words.append("".join(self.word))
            print(self.words)
            self.word = []
            self.cur_letters = self.letters

    def scoreGame(self):
        for word in self.words:
            for c in word:
                self.score += getScoreForLetter(c)
        self.scored = True

    def stopRunning(self):
        self.running = False;
        self.scoreGame()

    def run(self):
        self.running = True

        time_limit = 2 # seconds
    
        t = Timer(time_limit, self.stopRunning)
        t.start()

        while not self.scored:
            pass
        print("Time's Up!")
        print("You got %i points!" %(self.score))

def loadDict(filename):
    f = open(filename, 'r')
    wordlist = []
    for word in f:
        wordlist.append(word.rstrip())
    f.close()
    return wordlist

def get_letters():
    letters = []
    for i in range(12):
        letters.append(random.choice("AD"))
        # letters.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    return letters

def getScoreForLetter(c):
    # TODO: put in scoring system
    return 1
    
if __name__ == '__main__':
    d = loadDict("dictionary.txt")
    game = WordGame(d)

    root = Tk()
    frame = Frame(root, width=100, height=100)
    frame.bind("<KeyRelease>", game.keyReleased)
    frame.focus_set()
    frame.pack()

    game.start()

    root.mainloop()
    

    
