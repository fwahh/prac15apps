actualMoves = [" " for x in range(10)] # initialize list to hold moves

playerLetter = "O"
aiLetter = "X"

def PrintBoard (movelist):
    partition = "-"*12
    emptySpaceRow = "   |   |   "
    filledRowSide = " "
    filledRowMiddle = " | "
    print(emptySpaceRow)
    print(filledRowSide + movelist[1] + filledRowMiddle + movelist[2] + filledRowMiddle + movelist[3] + filledRowSide)
    print(emptySpaceRow)
    print(partition)
    print(emptySpaceRow)
    print(filledRowSide + movelist[4] + filledRowMiddle + movelist[5] + filledRowMiddle + movelist[6] + filledRowSide)
    print(emptySpaceRow)
    print(partition)
    print(emptySpaceRow)
    print(filledRowSide + movelist[7] + filledRowMiddle + movelist[8] + filledRowMiddle + movelist[9] + filledRowSide)
    print(emptySpaceRow)

def InsertLetter(letter,pos):
    actualMoves[pos] = letter

def IsMoveValid(pos):
    warning = "That is not a valid input"
    try:
        if pos in range(1,10):
            return actualMoves[pos] == " "
        else:
            return warning
    except:
        return warning

def IsBoardFull(movelist):
    return movelist.count(" ") == 1 #only movelist[0] will be empty space

def IsWinner(b,letter):
    return (b[1] == letter and b[2] == letter and b[3] == letter) or \
    (b[4] == letter and b[5] == letter and b[6] == letter) or \
    (b[7] == letter and b[8] == letter and b[9] == letter) or \
    (b[1] == letter and b[4] == letter and b[7] == letter) or \
    (b[2] == letter and b[5] == letter and b[8] == letter) or \
    (b[3] == letter and b[6] == letter and b[9] == letter) or \
    (b[1] == letter and b[5] == letter and b[9] == letter) or \
    (b[3] == letter and b[5] == letter and b[7] == letter)

def SelectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln )
    return li[r]

def PlayerMove():
    while True:
        playerInput = input("Please select an integer between 1 and 9 to place your move\n")

        move = IsMoveValid(int(playerInput))
        if move == True:
            InsertLetter(playerLetter, int(playerInput))
            break
        elif move == False:
            print ("This space is already taken")
        else:
            print (move)

def AIMove():
    possibleMoves = [x for x, letter in enumerate(actualMoves) if letter == " " and x != 0]
    move = 0

    for letter in [aiLetter, playerLetter]:
        for i in possibleMoves:
            boardcopy = actualMoves[:]
            boardcopy[i] = letter
            if IsWinner(boardcopy,letter):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = SelectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = SelectRandom(edgesOpen)
        return move

def TicTacToeGame():
    print ("Welcome to the game!")
    PrintBoard(actualMoves)
    while not (IsBoardFull(actualMoves)):
        if not(IsWinner(actualMoves,aiLetter)):
            PlayerMove()
            PrintBoard(actualMoves)
        else:
            print("You lose!")
            break
        if not(IsWinner(actualMoves,playerLetter)):
            move = AIMove()
            if move == 0:
                print (" ")
            else:
                InsertLetter(aiLetter , move)
                print ('Computer placed a %s on position %s :'%(aiLetter, move))
                PrintBoard(actualMoves)
        else:
            print ("You win!")
            break
    if IsBoardFull(actualMoves):
        print ("It's a tie!")

while True:
    gostop = input("Do you want to play a game (y/n)")
    if gostop.lower() == 'y':
        actualMoves = [" " for x in range(10)]
        print ("-"*20)
        TicTacToeGame()
    else:
        break
#problem: prog terminates when another letter is input, how to stop that?
#problem2: prog breaks when a tie is reached. why?
