class Board(object):
    game_board = [["", "", ""],
                ["" , "" , "" ],
                ["" , "" , "" ]]

    def print_board(self):
        for i in self.game_board:
            print i

class Player(object):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

class Game(object):
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.whos_next = player1

    def move(self, x, y):
        self.board.game_board[int(x)][int(y)] = self.whos_next.mark
        self.switch_players()
        self.board.print_board()

    def switch_players(self):
        if self.whos_next == player1:
            self.whos_next = player2
        else:
            self.whos_next = player1

    def is_not_finished(self):
        for x in range(3):
            for y in range(3):
                if self.board.game_board[x][y] == "":
                    return True
        return False

    def is_not_winner(self):
        return not self.check_horizontal() and not self.check_vertical() and not self.check_left_to_right_diagonal()

    def check_horizontal(self):
        for row in range(3):
            if len(set(self.board.game_board[row])) == 1 and self.board.game_board[row][0] is not "":
                return True
        return False

    def check_vertical(self):
        for column in range(3):
            if len(set([row[column] for row in self.board.game_board])) == 1 and self.board.game_board[0][column] is not "":
                return True
        return False

    def check_left_to_right_diagonal(self):
        if len(set([self.board.game_board[num][num] for num in range(3)])) == 1 and self.board.game_board[0][0] is not "":
            return True
        return False

    # TODO: Add check right to left diagonal

    def play(self):
        while self.is_not_finished() and self.is_not_winner():
            x = raw_input(self.whos_next.name + ", enter your x coordinate:")
            y = raw_input(self.whos_next.name + ", enter your y coordinate:")
            self.move(x, y)
        if not self.is_not_winner():
            if self.whos_next == player1:
                print player2.name + " won!"
            else:
                print player1.name + " won!"
        elif not self.is_not_finished():
            print "Awk...looks like no one won..."


if __name__ == '__main__':
    print "*" * 50
    print "Welcome to Anna's Version of Tic-Tac-Toe!"
    print "*" * 50
    name1 =raw_input("Player 1: Please enter your name:")
    player1 = Player(name1, "X")
    name2 = raw_input("Player2: Please enter your name:")
    player2 = Player(name2, "O")
    print "Thanks for playing " + player1.name + " and " + player2.name
    game = Game(player1, player2)
    game.board.print_board()

    game.play()

