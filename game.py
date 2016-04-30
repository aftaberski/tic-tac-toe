class Board(object):
    game_board = [["", "", ""],
                ["" , "" , "" ],
                ["" , "" , "" ]]

    def print_board(self):
        for i in self.game_board:
            print i

class Player(object):
    def __init__(self, name):
        self.name = name

class Game(object):
    def __init__(self, player1, player2, board):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.whos_next = player1

    # player needs to go
    # if the role was valid needs to rerender
    # needs to rerender the board
    # other player needs to go
    # rerender the board

    # all while checking 'is there a winner'
    # is the board full?
    #

if __name__ == '__main__':
    print "This is when I play tic-tac-toe"