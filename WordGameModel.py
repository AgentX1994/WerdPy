# Programmed John Asper (AgentX1994) 2016
# Werd Nerd originally by Porter Venn

import random
from threading import Thread, Timer

class WordGameModel:

    def __init__(self, d, controller):
        self.dict = d
        self.letters = get_letters()     # The 12 selected letters
        print(self.letters)
        self.cur_letters = get_letters() # A copy for the current word
        self.word = []                   # The word that is currently being spelled
        self.words = []                  # Words that have been spelled
        self.waiting = False             # Penalty waiting after entering the same word twice
        self.controller = controller     # The parent controller

    def keyReleased(self, event):
        if self.waiting:
            return
        c = event.char
        if c.upper() in self.cur_letters:
            print(c.upper())
            self.word.append(c.upper())
            self.cur_letters.remove(c.upper())
            self.controller.updateCurrentWord(''.join(self.word))
        elif event.keysym == 'Return':
            w = "".join(self.word)
            if not w in self.words:
                self.words.append(w)
                self.word = []
                self.cur_letters = self.letters
                self.controller.updateWordlistLabel(w, len(self.words)-1)
                self.controller.updateCurrentWord('')
            else:
                print("Woops, Repeated word!")
                self.waiting = True
                self.word = []
                self.cur_letters = self.letters
                t = Timer(3,self.endPenalty)
                t.start()
        elif event.keysym == 'Backspace':
            self.cur_letters.append(self.word.pop())
            self.controller.updateCurrentWord(''.join(self.word))
            

    def endPenalty(self):
        self.waiting = False
        self.controller.updateCurrentWord('')

    def scoreGame(self):
        score = 0
        for word in self.words:
            if not word in self.dict:
                score -= 5
            else:
                for c in word:
                    score += getScoreForLetter(c)
        return score

def get_letters():
    letters = []
    for i in range(12):
        letters.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    return letters

def getScoreForLetter(c):
    # TODO: put in scoring system
    return 1



    
