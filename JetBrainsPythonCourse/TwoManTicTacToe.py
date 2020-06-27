def printBoard(gameEntry):
    borders = "---------"
    print(borders)
    for row in gameEntry:
        print("| " + " ".join(row) + " |")
    print(borders)

def isWinner(gameEntry, playerMove):
    # check for vertical wins
    for j in range(3):
        if(gameEntry[0][j] == gameEntry[1][j] == gameEntry[2][j] == playerMove):
            return True
    # check for horizontal wins
    for row in gameEntry:
        if set(row) == {playerMove}:
            return True
    #check for diagonal wins
    if ((gameEntry[0][0] == gameEntry[1][1] == gameEntry[2][2] == playerMove) or
        (gameEntry[2][0] == gameEntry[1][1] == gameEntry[0][2] == playerMove)):
        return True

def isDraw():
    return all([entry != " " for row in gameEntry for entry in row])

def placeMove(i , j, playerMove):
    # i denotes row and j denotes column, both start from 1
    if gameEntry[i - 1][j - 1] == " ":
        gameEntry[i - 1][j - 1] = playerMove
        return True

def promptEntry(playerMove):
    i, j = 0, 0
    while True:
        try:
            i,j = [int(entry) for entry in input("Enter coordinates:").split()]
            if i not in range(1,4) or j not in range(1,4):
                print("Coordinates should be from 1 to 3!")
            else:
                if (placeMove(i,j,playerMove)):
                    printBoard(gameEntry)
                    break
                else:
                    print("This cell is occupied! Choose another one!")
        except ValueError:
            print("You should enter numbers!")

playerMoves = ["X","O"]
gameEntry = [[" ", " ", " "] for i in range(0,9,3)]
printBoard(gameEntry)

game_active = True
while game_active:
    for playerMove in playerMoves:
        promptEntry(playerMove)
        if isWinner(gameEntry, playerMove):
            print(playerMove + " wins")
            game_active = False
            break
        elif isDraw():
            print("Draw")
            game_active = False
            break
