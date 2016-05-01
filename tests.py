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

    def game_is_over(self):
        self.game.board.game_board = [["X", "O", ""],
                                    ["O", "X", ""],
                                    ["", "", "X"]]
        self.assertEqual(True, self.game.is_not_finished())
        # self.board.board = [[HUMAN, EMPTY, COMPUTER],
        #                     [HUMAN, HUMAN, HUMAN],
        #                     [COMPUTER, COMPUTER, EMPTY]]
        # self.assertEqual(HUMAN, self.board.get_winner())

        # self.board.board = [[COMPUTER, HUMAN, COMPUTER],
        #                     [COMPUTER, HUMAN, COMPUTER],
        #                     [HUMAN, COMPUTER, HUMAN]]
        # self.assertEqual(EMPTY, self.board.get_winner())

        # self.board.board = [[EMPTY, HUMAN, COMPUTER],
        #                     [COMPUTER, HUMAN, COMPUTER],
        #                     [EMPTY, COMPUTER, HUMAN]]
        # self.assertEqual(None, self.board.get_winner())

        # self.board.board = [[EMPTY, HUMAN, COMPUTER],
        #                     [HUMAN, COMPUTER, HUMAN],
        #                     [COMPUTER, COMPUTER, HUMAN]]
        # self.assertEqual(COMPUTER, self.board.get_winner())

        # self.board.board = [[EMPTY, HUMAN, HUMAN],
        #                     [HUMAN, COMPUTER, HUMAN],
        #                     [COMPUTER, COMPUTER, COMPUTER]]
        # self.assertEqual(COMPUTER, self.board.get_winner())

        # self.board.board = [[EMPTY, HUMAN, HUMAN],
        #                     [HUMAN, COMPUTER, HUMAN],
        #                     [COMPUTER, COMPUTER, COMPUTER]]
        # self.assertEqual(COMPUTER, self.board.get_winner())

        # self.board.board = [[HUMAN, COMPUTER, HUMAN],
        #                     [HUMAN, COMPUTER, HUMAN],
        #                     [HUMAN, HUMAN, COMPUTER]]
        # self.assertEqual(HUMAN, self.board.get_winner())

        # self.board.board = [[HUMAN, COMPUTER, HUMAN],
        #                     [COMPUTER, COMPUTER, HUMAN],
        #                     [HUMAN, EMPTY, HUMAN]]
        # self.assertEqual(HUMAN, self.board.get_winner())

if __name__ == '__main__':
    main()
