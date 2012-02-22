from tennis import Set
from unittest import TestCase

class TestSetWinning(TestCase):
    def test_score_names(self):
        set = Set()
        self.assertEqual("0", set.firstScore())
        set.firstScores()
        self.assertEqual("15", set.firstScore())
        set.firstScores()
        self.assertEqual("30", set.firstScore())
        set.firstScores()
        self.assertEqual("40", set.firstScore())
