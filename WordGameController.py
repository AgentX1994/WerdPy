#! /usr/bin/env python3
from threading import Timer, Thread
from tkinter import *
from WordGameModel import WordGameModel
import json

time_per_game = 10 # seconds

class WordGameController:

    def __init__(self, d, s):
        Thread.__init__(self)
        self.dict = d
        self.scoring = s
        print("The loaded dictionary is ")
        print(d)
        self.running = False
        self.game = None

    def newGame(self):
        self.running = True
        for v in word_variables:
            v.set("")
        self.game = WordGameModel(self.dict, self.scoring, self)
        self.timer = Timer(time_per_game, self.stopGame)
        self.timer.start()

    def stopGame(self):
        self.running = False
        scoreVar.set("Your score is %i"%(int(self.game.scoreGame())))

    def keyReleased(self, event):
        if self.running and self.game:
            self.game.keyReleased(event)
        elif self.running and not self.game:
            raise Exception("The game controller is running but has no game. This shouldn't happen.")

    def updateWordlistLabel(self, word, index):
        word_variables[index].set(word)

    def updateCurrentWord(self, word):
        currentWordVar.set(word)
    
def loadDict(filename):
    with open(filename, 'r') as f:
        wordlist = []
        for word in f:
            wordlist.append(word.rstrip().upper())
        f.close()
    return wordlist
    
if __name__ == '__main__':
    d = loadDict("dictionary.txt")
    with open('pyWerdScores.json') as data_file:
        s = json.load(data_file)
    
    gameController = WordGameController(d, s)

    root = Tk()
    root.title("pyWerd")
    root.geometry("800x600+400+400")
    container = Frame(root, background='white')
    container.bind("<KeyRelease>", gameController.keyReleased)
    container.focus_set()
    container.pack(fill=BOTH, expand=1)

    wordlistFrame = Frame(container,background='black')
    for i in range(4):
        wordlistFrame.columnconfigure(i, pad=5, weight=1)
    for i in range(15):
        wordlistFrame.rowconfigure(i, pad=3, weight=1)
    word_variables = [StringVar() for x in range(60)]
    word_labels = [Label(wordlistFrame, textvariable=word_variables[x], bg='white', width=800//4-173) for x in range(60)]
    
    i = 0
    for l in word_labels:
        word_variables[i].set("")
        l.grid(row=(i%15),column=(i//15))
        i = i + 1

    wordlistFrame.pack(fill=BOTH, side=TOP)

    currentWordVar = StringVar()
    currentWord = Label(container, textvariable=currentWordVar, bg='white')
    currentWord.pack(side=BOTTOM, padx=5, pady=5)

    scoreVar = StringVar()
    scoreLbl = Label(container, textvariable=scoreVar, bg='white')
    scoreLbl.pack(side=LEFT,anchor=S,padx=5,pady=5)

    newGameButton = Button(container, text="New Game",
                           command = gameController.newGame)
    newGameButton.pack(side=RIGHT,anchor=S,padx=5,pady=5)

    root.mainloop()
    
