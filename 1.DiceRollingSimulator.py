import random

diceValue = random.randint(1,6)

def printDice(value):  #function to print the dice depending on the value fed in
    print(' '+'-'*11)
    if value == 1:
        print (' '+'|'+' '*9 + '|')
        print (' '+'|'+' '*4 + 'o' +' '*4 + '|')
        print (' '+'|'+' '*9 + '|')
    elif value == 2:
        print (' '+'|'+' '*9 + '|')
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
        print (' '+'|'+' '*9 + '|')
    elif value == 3:
        print (' '+'|'+' '*4 + 'o' +' '*4 + '|')
        print (' '+'|'+' '*4 + 'o' +' '*4 + '|')
        print (' '+'|'+' '*4 + 'o' +' '*4 + '|')
    elif value == 4:
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
        print (' '+'|'+' '*9 + '|')
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
    elif value == 5:
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
        print (' '+'|'+' '*4 + 'o' +' '*4 + '|')
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
    elif value == 6:
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')
        print (' '+'|'+' '*2 + 'o' +' '*3 + 'o' +' '*2+ '|')

    print(' '+'-'*11)
flag = 'y'
# Following is for user interaction
flag = input("Hello traveller, this is a random dice simulator, if you would like to give it a try, please enter the 'y' key.")
while flag == 'y':
    diceValue = random.randint(1,6)
    printDice(diceValue)
    flag = input("You have chosen to roll the die, if you would like to continue, enter the 'y' key again.")

if flag != 'y':
    print('You have chosen not to continue. I bid you good day.')
