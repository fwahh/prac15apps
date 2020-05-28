import random #to randomize choice of words
import json #module required to load json file

#to populate the list of possible words
dictionaryData = json.load(open("dictionarydata.json"))
wordlist = list(dictionaryData.keys())

#initializing variables
wordlength = 0
minimumletters = 4
turns = 10
correctGuesses = "" #to keep track of correct letters guessed, intialized outside of loop
validLetters = "abcdefghijklmnopqrstuvwxyz"
correctWord = random.choice(wordlist)

#function to ensure phrase doesn't have weird char
def SaneWord(word):
    for letter in word:
        if letter not in validLetters and letter != " ":
            return False
            break
    return True

#to ensure the populated word is not too short and doesn't have weird char
while wordlength <= minimumletters and SaneWord(correctWord) != True:
    correctWord = random.choice(wordlist)
    wordlength = len(correctWord)

#function to print hangman
def PrintHangman(guessesleft):
    print("  --------  ")
    if guessesleft == 8:
        print("     O      ")
    if guessesleft == 7:
        print("     O      ")
        print("     |      ")
    if guessesleft == 6:
        print("     O      ")
        print("     |      ")
        print("    /       ")
    if guessesleft == 5:
        print("     O      ")
        print("     |      ")
        print("    / \     ")
    if guessesleft == 4:
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
    if guessesleft == 3:
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
    if guessesleft == 2:
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
    if guessesleft == 1:
        print("   \ O_|/   ")
        print("     |      ")
        print("    / \     ")
    if guessesleft == 0:
        print("     O_|    ")
        print("    /|\      ")
        print("    / \     ")
    if guessesleft >= 2:
        print("%s chances remaining" %(guessesleft))
        print("-"*80)
    elif guessesleft == 1:
        print ("1 last chance remaining! A single misstep and he dies")
        print("-"*80)

#interaction with user
print("")
print ("Kind adventurer, please help me! My cousin has been taken by the brutish")
print("king and will be hanged unless I play along with his silly game. To save him,")
print("We have to guess the phrase in his mind.")
print("We only have 10 chances for any mistakes.")
print("-"*34+"Game Start!"+"-"*34)
print("The king's thinking of: " + "_ "*len(correctWord))
print("-"*80)
#start the loop
while len(correctWord) >= minimumletters:
    guess = input("Enter a letter to guess\n")
    currentStatus = ""

    if guess not in validLetters or len(guess) > 1: #check validity of input
        print("Please don't be like this. The king will overlook this. Enter a valid guess!")
        print("-"*80)
    elif guess in correctGuesses:
        print ("You have already guessed that!")
        print("-"*80)
    else:
        if guess in correctWord:
            correctGuesses = correctGuesses + guess #keeping track of correct letters guessed

        for letter in correctWord:
            if letter in correctGuesses: #printing out letters already guessed
                currentStatus = currentStatus + letter + " "
            elif letter == " ":
                currentStatus = currentStatus + " "
            else: #remaining unguessed words
                currentStatus = currentStatus + "_" + " "
        print ("The king's thinking of: " + currentStatus)

        if currentStatus.replace(" ","") == correctWord.replace(" ",""):
            print("He lives!")
            break
        elif guess in correctWord:
            print("You guessed right! Good job! Keep going!")
            print("-"*80)
        else:
            print("Nooo, that was a mistake")
            turns -= 1
            PrintHangman(turns)
            if turns == 0:
                print("You....you let him die. The correct phrase was " + correctWord)
                break
