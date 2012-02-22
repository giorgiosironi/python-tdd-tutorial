class Set:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.scores = Scores()
    def firstScores(self, times=1):
        self.first = self.first + times
    def firstScore(self):
        return self.scores.scoreName(self.first)
    def secondScores(self, times=1):
        self.second = self.second + times
    def secondScore(self):
        return self.scores.scoreName(self.second)
    def winner(self):
        if (self.first > 3 and self.second < 3):
            return 1
        if (self.second > 3 and self.first < 3):
            return 2
        if (self.first > 4 and self.second < 4):
            return 1
        return None

class Scores:
    def __init__(self):
        self.scoreNames = ["0", "15", "30", "40", "A"]
    def scoreName(self, index):
        return self.scoreNames[index]
