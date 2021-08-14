import random
import sys
import os
import time

germanWordList = []
englishWordList = []

def sinput(prompt):
 temp = input(prompt)
 time.sleep (0.2)
 return temp

def initVocab():
    vocabFile = open("vocab.txt","r")
    vocabList = []
    for line in vocabFile:
        vocabList.append(line)
    print(vocabList)
    german = True
    germanWordString = ""
    english = False
    englishWordString = ""
    for line in range (len(vocabList)):
        for char in vocabList[line]:
            if char == "-" or char == '\n' :
                if german:
                    english = True
                    german = False
                    germanWordList.append(germanWordString)
                    germanWordString = ""
                    continue
                else:
                    english = False
                    german = True
                    englishWordList.append(englishWordString)
                    englishWordString = ""
                    continue
            if german:
                germanWordString += char
            if english:
                englishWordString += char

def startTest(questionsMode):
    os.system('clear')
    if questionsMode == False:
        while True:
            randomNum = random.randint(0,(len(germanWordList)-1))
            wait = sinput("German: "+str(germanWordList[randomNum]+"\n"))
            if wait == "q":
                return
            wait = sinput(("Answer: "+englishWordList[randomNum]+"\n"))
            os.system('clear')
    else:
        questionsCorrect = 0
        score = 0
        numberQuestions = int(sinput("Number of questions : "))

        print('Enter y/n when answer is shown to mark answer')
        for i in range (numberQuestions):
            
            randomNum = random.randint(0,(len(germanWordList)-1))
            wait = sinput("German: "+str(germanWordList[randomNum]+"\n"))
            if wait == "q":
                return
            wait = sinput(("Answer: "+englishWordList[randomNum]+"\n"))
            validInput = False
            while validInput == False:
             print('while')
             if wait == 'y':
              score += 1
              validInput = True
             if wait == 'n':
              validInput = True
             else:
              wait = sinput('Invalid - Please enter y/n')
            os.system('clear')
        print('Score',score,'/',numberQuestions)
        print('Percent: ',str(numberQuestions/score))        

def menu():
    while True:
        os.system('clear')
        menuChoice = int(sinput("""
        1. Start Vocab Test (Infinite)
        2. Start Question Test
        0. Exit\n"""))
        if menuChoice == 1:
            startTest(False)
        if menuChoice == 2:
           startTest(True)
        else:
            sys.exit()
    
initVocab()
menu()