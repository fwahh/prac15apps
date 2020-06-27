import random

acceptable_input = ('user', 'easy', 'medium')

class TicTacToe:
    borders = "---------"
    moves = ('X','O')

    def __init__(self, player1, player2):
        self.gameEntry = [[" ", " ", " "] for i in range(0,9,3)]
        self.game_active = True
        self.player1 = player1
        self.player2 = player2
        self.printBoard()

    def printBoard(self):
        print(TicTacToe.borders)
        for row in self.gameEntry:
            print("| " + " ".join(row) + " |")
        print(TicTacToe.borders)

    def placeMove(self, i , j, move, board):
        if board[-j][i-1] == " ":
            board[-j][i - 1] = move
            return True
        return False

    def promptEntry(self, playerMove):
        while True:
            try:
                i,j = [int(entry) for entry in \
                input("Enter the coordinates:").split()]
                if i not in range(1,4) or j not in range(1,4):
                    print("Coordinates should be from 1 to 3!")
                else:
                    if self.placeMove(i, j, playerMove, self.gameEntry):
                        self.printBoard()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
            except ValueError:
                print("You should enter numbers!")

    def randomMove(self, aiMove):
        while True:
            i = random.randint(1,3)
            j = random.randint(1,3)
            if self.placeMove(i, j, aiMove, self.gameEntry):
                return i,j
    def easyAIMove(self, aiMove):
        self.randomMove(aiMove)
        print('Making move level "easy"')
        self.printBoard()

    def WinningMove(self, moveNum):
        for move in (TicTacToe.moves[moveNum],TicTacToe.moves[1 - moveNum]):
            for i in range(1,4):
                for j in range(1,4):
                    testEntry = [row[:] for row in self.gameEntry]
                    if self.placeMove(i, j, move, testEntry):
                        if self.isWinner(move, testEntry):
                            return i,j
        else:
            return False

    def mediumAIMove(self, aiMove):
        if aiMove == TicTacToe.moves[0]:
            moveNum = 0
        else:
            moveNum = 1
        deterministicMove = self.WinningMove(moveNum)
        if deterministicMove == False:
            self.randomMove(aiMove)
        else:
            self.placeMove(deterministicMove[0], deterministicMove[1],
                aiMove, self.gameEntry)
        print ('Making move level "medium"')
        self.printBoard()

    def isWinner(self, move, board):
        # check for vertical wins
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == move:
                return True
        # check for horizontal wins
        for row in board:
            if set(row) == {move}:
                return True
        #check for diagonal wins
        if ((board[0][0] == board[1][1] == board[2][2] == move) or
            (board[2][0] == board[1][1] == board[0][2] == move)):
            return True

    def isDraw(self):
        return all([entry in TicTacToe.moves for row in self.gameEntry \
            for entry in row])

    def playGame(self):
        corresponding_moves = (self.promptEntry, self.easyAIMove,
            self.mediumAIMove)
        menu = dict(zip(acceptable_input, corresponding_moves))
        self.game_active = True
        i = 0
        gameMoves = (menu[self.player1], menu[self.player2])
        while self.game_active:
            gameMove = gameMoves[i]
            move = TicTacToe.moves[i]
            gameMove(move)
            if self.isWinner(move, self.gameEntry):
                print(move, "wins")
                self.game_active = False
            elif self.isDraw():
                print ("Draw")
                self.game_active = False
            i = 1 - i
while True:
    command = input('Input command: ').split()
    if len(command) == 1 and command[0] == 'exit':
        break
    elif (len(command) == 3 and command[0] == 'start' and
        command[1] in acceptable_input and
        command[2] in acceptable_input):
        starto = TicTacToe(command[1], command[2])
        starto.playGame()
    else:
        print("Bad parameters!")
