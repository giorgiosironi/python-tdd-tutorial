class Set:
    def __init__(self):
        self.first = 0
        self.scoreNames = ["0", "15", "30", "40"]
    def firstScores(self):
        self.first = self.first + 1
    def firstScore(self):
        return self.scoreNames[self.first]
