import random

acceptable_input = ('user', 'easy', 'medium')

class TicTacToe:
    borders = "-" * 9
    moves = ('X','O')

    def __init__(self, player1, player2):
        self.gameEntry = [" " for i in range(0,9)]
        self.game_active = True
        self.player1 = player1
        self.player2 = player2
        self.printBoard()

    def printBoard(self):
        print(TicTacToe.borders)
        for i in range(0,9,3):
            print("| " + " ".join(self.gameEntry[i:i + 3]) + " |")
        print(TicTacToe.borders)

    def placeMove(self, boardindex, move, board):
        if board[boardindex] == " ":
            board[boardindex] = move
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
                    boardindex = i - 1 + 3 * (3 - j)
                    if self.placeMove(boardindex, playerMove, self.gameEntry):
                        self.printBoard()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
            except ValueError:
                print("You should enter numbers!")

    def randomMove(self, aiMove):
        while True:
            boardindex = random.randint(0,8)
            if self.placeMove(boardindex, aiMove, self.gameEntry):
                return boardindex

    def easyAIMove(self, aiMove):
        self.randomMove(aiMove)
        print('Making move level "easy"')
        self.printBoard()

    def WinningMove(self, moveNum):
        possibleMoves = [i for i in range(9) if self.gameEntry[i] == " "]
        for move in (TicTacToe.moves[moveNum],TicTacToe.moves[1 - moveNum]):
            for i in possibleMoves:
                testEntry = self.gameEntry[:]
                self.placeMove(i, move, testEntry)
                if self.isWinner(move, testEntry):
                    return i
        else:
            return False

    def mediumAIMove(self, aiMove):
        moveNum = 0 if aiMove == TicTacToe.moves[0] else 1
        deterministicMove = self.WinningMove(moveNum)
        if deterministicMove == False:
            self.randomMove(aiMove)
        else:
            self.placeMove(deterministicMove, aiMove, self.gameEntry)
        print ('Making move level "medium"')
        self.printBoard()

    def isWinner(self, move, board):
        winningCondition = [board[:3], board[3:6], board[6:],
            board[::3], board[1::3], board[2::3],
            board[:9:4], board[2:7:2]]
        if [move, move, move] in winningCondition:
            return True

    def isDraw(self):
        return all([entry in TicTacToe.moves for entry in self.gameEntry])

    def playGame(self):
        corresponding_moves = (self.promptEntry, self.easyAIMove,
            self.mediumAIMove)
        menu = dict(zip(acceptable_input, corresponding_moves))
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
