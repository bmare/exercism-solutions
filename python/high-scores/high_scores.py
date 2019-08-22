class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sortedScores = scores[:]
        self.sortedScores.sort(reverse = True)
    def latest (self):
        return self.scores[-1]
    def personal_best(self):
        return self.sortedScores[0]
    def personal_top_three(self):
        return self.sortedScores[0:3]
