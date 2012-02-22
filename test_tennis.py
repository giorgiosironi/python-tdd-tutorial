from tennis import Set, Scores
from unittest import TestCase

class TestSetWinning(TestCase):
    def test_score_grows(self):
        set = Set()
        self.assertEqual("0", set.firstScore())
        set.firstScores()
        self.assertEqual("15", set.firstScore())
        self.assertEqual("0", set.secondScore())
        set.secondScores()
        self.assertEqual("15", set.secondScore())
    def test_player_1_win_when_scores_at_40(self):
        set = Set()
        set.firstScores(3)
        self.assertEqual(None, set.winner())
        set.firstScores()
        self.assertEqual(1, set.winner())
    def test_player_2_win_when_scores_at_40(self):
        set = Set()
        set.secondScores(3)
        self.assertEqual(None, set.winner())
        set.secondScores()
        self.assertEqual(2, set.winner())
    def test_deuce_requires_more_than_one_ball_to_win(self):
        set = Set()
        set.firstScores(3)
        set.secondScores(3)
        set.firstScores()
        self.assertEqual(None, set.winner())
        set.firstScores()
        self.assertEqual(1, set.winner())

class TestScoreNames(TestCase):
    def test_score_names(self):
        scores = Scores()
        self.assertEqual("0", scores.scoreName(0))
        self.assertEqual("15", scores.scoreName(1))
        self.assertEqual("30", scores.scoreName(2))
        self.assertEqual("40", scores.scoreName(3))
        self.assertEqual("A", scores.scoreName(4))
