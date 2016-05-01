from unittest import TestCase, main
from game import Board, Player, Game

class TestGame(TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("Michael Jordan", "X")
        self.player2 = Player("Marvin The Martian", "O")
        self.game = Game(self.player1, self.player2)

    def test_who_won(self):
        # Test left to right diagonal
        self.game.board.game_board = [["X", "O", ""],
                                    ["O", "X", ""],
                                    ["", "", "X"]]
        self.assertEqual(False, self.game.is_not_winner())

        # Test vertical win
        self.game.board.game_board = [["", "O", "X"],
                                    ["O", "X", "X"],
                                    ["", "O", "X"]]
        self.assertEqual(False, self.game.is_not_winner())

        # Test horizontal win
        self.game.board.game_board = [["O", "O", "O"],
                                    ["O", "X", "X"],
                                    ["", "X", "X"]]
        self.assertEqual(False, self.game.is_not_winner())

    def test_is_finished(self):
        self.game.board.game_board = [["X", "O", ""],
                                      ["O", "X", ""],
                                      ["", "O", ""]]
        self.assertEqual(True, self.game.is_not_finished())

        self.game.board.game_board = [["X", "O", "O"],
                                      ["O", "X", "X"],
                                      ["O", "O", "O"]]
        self.assertEqual(False, self.game.is_not_finished())

if __name__ == '__main__':
    main()
