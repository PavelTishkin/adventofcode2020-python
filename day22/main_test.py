import unittest

from day22 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.decks_txt = [
            'Player 1:', '9', '2', '6', '3', '1', '',
            'Player 2:', '5', '8', '4', '7', '10'
        ]

    def test_load_decks_returns_correct_decks(self):
        deck1, deck2 = main.load_decks(self.decks_txt)
        self.assertEqual(deck1, [9, 2, 6, 3, 1])
        self.assertEqual(deck2, [5, 8, 4, 7, 10])

    def test_play_round_returns_correct_decks(self):
        deck1, deck2 = main.load_decks(self.decks_txt)
        deck1, deck2 = main.play_round(deck1, deck2)
        self.assertEqual(deck1, [2, 6, 3, 1, 9, 5])
        self.assertEqual(deck2, [8, 4, 7, 10])

    def test_play_game_returns_correct_deck(self):
        deck1, deck2 = main.load_decks(self.decks_txt)
        deck, winner, rounds = main.play_game(deck1, deck2)
        self.assertEqual(deck, [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
        self.assertEqual(winner, 2)
        self.assertEqual(rounds, 29)

    def test_calculate_score_returns_correct_score(self):
        deck1, deck2 = main.load_decks(self.decks_txt)
        deck, _, _ = main.play_game(deck1, deck2)
        actual = main.calculate_score(deck)
        self.assertEqual(actual, 306)

    def test_play_rec_game_stops_on_infinite_loop(self):
        deck1, deck2 = main.load_decks(['Player 1:', '43', '19', '', 'Player 2:', '2', '29', '14'])
        deck1, deck2, winner, insta_win = main.play_rec_game(deck1, deck2)
        self.assertEqual(winner, 1)
        self.assertEqual(insta_win, True)

    def test_play_rec_game_returns_correct_winner(self):
        deck1, deck2 = main.load_decks(self.decks_txt)
        deck1, deck2, winner, insta_win = main.play_rec_game(deck1, deck2)
        if winner == 1:
            score = main.calculate_score(deck1)
        else:
            score = main.calculate_score(deck2)
        self.assertEqual(winner, 2)
        self.assertEqual(deck2, [7, 5, 6, 2, 4, 1, 10, 8, 9, 3])
        self.assertEqual(score, 291)

