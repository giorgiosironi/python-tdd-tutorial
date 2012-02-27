class Set:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.scores = Scores()
    def firstScores(self, times=1):
        self.first = self.first + times
        self._normalizeScores()
    def firstScore(self):
        return self.scores.scoreName(self.first)
    def secondScores(self, times=1):
        self.second = self.second + times
        self._normalizeScores()
    def secondScore(self):
        return self.scores.scoreName(self.second)
    def winner(self):
        if self._isWinning(self.first, self.second):
            return 1
        if self._isWinning(self.second, self.first):
            return 2
        return None
    def _isWinning(self, winner, loser):
        return winner > 3 and winner - loser >= 2
    def _normalizeScores(self):
        if (self.first == self.scores.maximum() and self.second == self.scores.maximum()):
            self.first = self.first - 1
            self.second = self.second - 1

class Scores:
    def __init__(self):
        self.scoreNames = ["0", "15", "30", "40", "A"]
    def scoreName(self, index):
        return self.scoreNames[index]
    def maximum(self):
        return 4
